# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Read-only GitHub evidence collector. PI/gpt-6.1-sol."""

import argparse
import base64
import concurrent.futures
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.parse

BOT_NAMES = {"dependabot", "renovate", "github-actions", "semantic-release-bot", "copybara-github", "cursoragent", "claude", "cursor", "codex", "copilot"}
CODE_SUFFIXES = {".py", ".ipynb", ".rs", ".ts", ".tsx", ".js", ".jsx", ".c", ".cpp", ".h", ".cu", ".sh", ".toml", ".yaml", ".yml", ".html", ".css", ".vue"}


def api(endpoint):
    env = os.environ.copy()
    env.pop("GH_TOKEN", None)
    env.pop("GITHUB_TOKEN", None)
    result = subprocess.run(["gh", "api", endpoint, "--cache", "3600s"], env=env, text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def human(person):
    login = person["login"].lower()
    return person["type"] == "User" and login not in BOT_NAMES and not login.endswith(("[bot]", "-bot"))


def collect(repo, root):
    directory = root / "github" / repo.replace("/", "__")
    directory.mkdir(parents=True, exist_ok=True)
    metadata = api(f"repos/{repo}")
    (directory / "metadata.json").write_text(json.dumps(metadata, indent=2))
    branch = urllib.parse.quote(metadata["default_branch"], safe="")
    commits = api(f"repos/{repo}/commits?sha={branch}&per_page=20")
    (directory / "commits.json").write_text(json.dumps(commits, indent=2))
    contributors = []
    page = 1
    while True:
        batch = api(f"repos/{repo}/contributors?per_page=100&page={page}")
        contributors.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    (directory / "contributors.json").write_text(json.dumps(contributors, indent=2))
    humans = [item for item in contributors if human(item)]
    issues = api(f"repos/{repo}/issues?state=all&per_page=10")
    releases = api(f"repos/{repo}/releases?per_page=5")
    (directory / "issues.json").write_text(json.dumps(issues, indent=2))
    (directory / "releases.json").write_text(json.dumps(releases, indent=2))
    readme = api(f"repos/{repo}/readme")
    (directory / "README.md").write_bytes(base64.b64decode(readme["content"]))
    latest_code = None
    for commit in commits:
        detail = api(f"repos/{repo}/commits/{commit['sha']}")
        paths = [item["filename"] for item in detail["files"]]
        if any(Path(path).suffix in CODE_SUFFIXES and not path.startswith(("docs/", ".github/")) for path in paths):
            latest_code = {"sha": commit["sha"], "date": commit["commit"]["committer"]["date"], "message": commit["commit"]["message"].splitlines()[0], "paths": paths}
            (directory / "latest_code_commit.json").write_text(json.dumps(detail, indent=2))
            break
    now = dt.datetime.now(dt.timezone.utc)
    def age(date):
        return (now - dt.datetime.fromisoformat(date.replace("Z", "+00:00"))).days
    row = {"repo": metadata["full_name"], "requested_repo": repo, "stars": metadata["stargazers_count"], "humans_estimate": len(humans), "top_humans": [item["login"] for item in humans[:5]], "created_at": metadata["created_at"], "project_age_days": age(metadata["created_at"]), "archived": metadata["archived"], "fork": metadata["fork"], "default_branch": metadata["default_branch"], "latest_commit": commits[0]["commit"]["committer"]["date"], "latest_commit_age_days": age(commits[0]["commit"]["committer"]["date"]), "latest_code_commit": latest_code, "latest_code_age_days": age(latest_code["date"]) if latest_code else None, "license": metadata["license"]["spdx_id"] if metadata["license"] else None, "issue_titles": [item["title"] for item in issues if "pull_request" not in item], "latest_release": releases[0]["tag_name"] if releases else None, "evidence_dir": str(directory), "retrieved_at": now.isoformat()}
    (directory / "summary.json").write_text(json.dumps(row, indent=2))
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repos", nargs="*")
    parser.add_argument("--readme", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repos = args.repos
    if args.readme:
        repos += ["/".join(pair) for pair in re.findall(r"https://github\.com/([^/\s)]+)/([^/\s)?#]+)", args.readme.read_text()) if pair[0] not in {"wassname", "topics"}]
    repos = list(dict.fromkeys(repos))
    args.output.mkdir(parents=True, exist_ok=True)
    rows, failures = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(collect, repo, args.output): repo for repo in repos}
        for future in concurrent.futures.as_completed(jobs):
            repo = jobs[future]
            try:
                row = future.result()
                rows.append(row)
                print(f"{repo}: humans*={row['humans_estimate']} stars={row['stars']} last_commit={row['latest_commit_age_days']}d archived={row['archived']}", flush=True)
            except (subprocess.CalledProcessError, ValueError, KeyError, IndexError) as error:
                failures.append({"repo": repo, "error": str(error), "stderr": error.stderr if isinstance(error, subprocess.CalledProcessError) else None})
                print(f"FAILED {repo}: {error}", flush=True)
    (args.output / "github_snapshot.json").write_text(json.dumps(sorted(rows, key=lambda row: (-row["humans_estimate"], -row["stars"])), indent=2))
    (args.output / "github_failures.json").write_text(json.dumps(failures, indent=2))
    print(f"Saved {len(rows)} repositories; {len(failures)} explicit failures. {args.output / 'github_snapshot.json'}", flush=True)
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()

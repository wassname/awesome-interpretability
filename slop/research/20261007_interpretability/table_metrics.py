# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Fetch public GitHub table metrics, not repository code. PI/gpt-6.1-sol."""

import argparse
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import subprocess

SERVICE_LOGINS = {"claude", "cursor", "codex", "copilot", "cursoragent", "copybara-github", "microsoftopensource", "msftgits", "interpret-ml", "aisi-inspect", "authensor", "imgbotapp"}


def api(endpoint):
    return json.loads(subprocess.check_output(["gh", "api", "--cache", "1h", endpoint], text=True))


def collect(repo):
    meta = api(f"repos/{repo}")
    if meta["private"]:
        return {"requested_repo": repo, "public": False}
    tip = api(f"repos/{repo}/commits?sha={meta['default_branch']}&per_page=1")[0]
    contributors = []
    page = 1
    while True:
        batch = api(f"repos/{repo}/contributors?per_page=100&page={page}")
        contributors.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    accounts = [p for p in contributors if p["type"] == "User" and p["login"].lower() not in SERVICE_LOGINS and not p["login"].lower().endswith(("[bot]", "-bot"))]
    return {"repo": meta["full_name"], "requested_repo": repo, "public": True, "stars": meta["stargazers_count"], "humans_estimate": len({p["id"] for p in accounts}), "accounts": [p["login"] for p in accounts], "created_at": meta["created_at"], "latest_commit": tip["commit"]["committer"]["date"], "latest_sha": tip["sha"], "branch": meta["default_branch"], "archived": meta["archived"], "fork": meta["fork"], "retrieved_at": dt.datetime.now(dt.timezone.utc).isoformat()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repos", nargs="+")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(collect, dict.fromkeys(args.repos)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"Saved {len(rows)} table records to {args.output}; private repository metrics omitted.")


if __name__ == "__main__":
    main()

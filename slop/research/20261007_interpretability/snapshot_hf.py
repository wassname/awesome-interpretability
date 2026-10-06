# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Snapshot public HF metadata and cards, never model tensors. PI/gpt-6.1-sol."""

import argparse
import datetime as dt
import json
from pathlib import Path
import urllib.error
import urllib.request


def fetch(url):
    with urllib.request.urlopen(url, timeout=45) as response:
        return response.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("specs", nargs="+", help="models:owner/name, datasets:owner/name or spaces:owner/name")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for spec in args.specs:
        kind, repo = spec.split(":", 1)
        assert kind in {"models", "datasets", "spaces"}, kind
        directory = args.output / kind / repo.replace("/", "__")
        directory.mkdir(parents=True, exist_ok=True)
        metadata = json.loads(fetch(f"https://huggingface.co/api/{kind}/{repo}"))
        (directory / "metadata.json").write_text(json.dumps(metadata, indent=2))
        prefix = {"models": "", "datasets": "datasets/", "spaces": "spaces/"}[kind]
        card_url = f"https://huggingface.co/{prefix}{repo}/raw/main/README.md"
        try:
            (directory / "README.md").write_bytes(fetch(card_url))
            card_status = "fetched"
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise
            card_status = "404: card absent"
        runtime = None
        if kind == "spaces":
            runtime = json.loads(fetch(f"https://huggingface.co/api/spaces/{repo}/runtime"))
            (directory / "runtime.json").write_text(json.dumps(runtime, indent=2))
        fields = {key: metadata[key] if key in metadata else None for key in ("id", "sha", "private", "gated", "likes", "downloads", "createdAt", "lastModified", "cardData", "safetensors")}
        fields.update(kind=kind, card_url=card_url, card_status=card_status, runtime=runtime, retrieved_at=dt.datetime.now(dt.timezone.utc).isoformat())
        rows.append(fields)
        print(f"{spec}: card={card_status}", flush=True)
    (args.output / "hf_snapshot.json").write_text(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()

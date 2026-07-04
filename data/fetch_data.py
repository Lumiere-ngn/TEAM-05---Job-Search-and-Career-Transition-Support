#!/usr/bin/env python3
"""Download job-posting datasets from Hugging Face into data/raw/."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from huggingface_hub import hf_hub_download, snapshot_download
except ImportError:
    print("Install dependencies: pip install -r requirements.txt", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
RAW.mkdir(parents=True, exist_ok=True)
MANIFEST = ROOT / "download_manifest.json"


DATASETS = [
    {
        "id": "xanderios/linkedin-job-postings",
        "files": ["job_postings.csv"],
        "method": "file",
    },
    {
        "id": "fact-den/indeed-job-postings-2026",
        "files": ["jobs/jobs.csv", "companies/companies.csv"],
        "method": "file",
    },
    {
        "id": "mindweave/job-postings-applications",
        "method": "snapshot",
    },
]


def download_file(repo_id: str, filename: str) -> Path:
    path = hf_hub_download(
        repo_id=repo_id,
        repo_type="dataset",
        filename=filename,
        local_dir=str(RAW / repo_id.replace("/", "__")),
    )
    return Path(path)


def download_snapshot(repo_id: str) -> Path:
    dest = RAW / repo_id.replace("/", "__")
    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        local_dir=str(dest),
    )
    return dest


def main() -> None:
    manifest: dict = {"downloaded": [], "errors": []}

    for spec in DATASETS:
        repo_id = spec["id"]
        print(f"Fetching {repo_id}...")
        try:
            if spec["method"] == "snapshot":
                dest = download_snapshot(repo_id)
                manifest["downloaded"].append(
                    {"repo": repo_id, "path": str(dest), "method": "snapshot"}
                )
            else:
                for filename in spec["files"]:
                    path = download_file(repo_id, filename)
                    manifest["downloaded"].append(
                        {
                            "repo": repo_id,
                            "file": filename,
                            "path": str(path),
                            "method": "file",
                        }
                    )
            print(f"  OK: {repo_id}")
        except Exception as exc:  # noqa: BLE001 — collect and continue
            msg = f"{repo_id}: {exc}"
            print(f"  FAILED: {msg}", file=sys.stderr)
            manifest["errors"].append(msg)

    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"\nManifest written to {MANIFEST}")
    if manifest["errors"]:
        print(f"Completed with {len(manifest['errors'])} error(s).", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

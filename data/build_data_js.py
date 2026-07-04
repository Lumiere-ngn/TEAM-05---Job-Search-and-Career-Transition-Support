#!/usr/bin/env python3
"""Build data.js from aggregated CSV/JSON for static HTML embedding."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent


def main() -> None:
    json_path = ROOT / "aggregated.json"
    if not json_path.exists():
        raise SystemExit("Run aggregate.py first to create aggregated.json")

    payload = json.loads(json_path.read_text())
    js = "window.JOB_FIT_DATA = " + json.dumps(payload, indent=2) + ";\n"
    (ROOT / "data.js").write_text(js)

    html_path = PROJECT / "index.html"
    html = html_path.read_text()

    # Replace inline DATA block or inject script tag
    script_tag = '<script src="data/data.js"></script>'
    if 'src="data/data.js"' not in html:
        html = html.replace("</head>", f"  {script_tag}\n</head>")

    # Remove old const DATA = {...}; block if present
    html = re.sub(
        r"const DATA = \{[\s\S]*?\};\s*\n",
        "",
        html,
        count=1,
    )

    html_path.write_text(html)
    print(f"Wrote {ROOT / 'data.js'}")
    print(f"Updated {html_path} to load data/data.js")


if __name__ == "__main__":
    main()

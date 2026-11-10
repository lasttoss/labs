#!/usr/bin/env python3
"""Generate the lab catalogue README from catalog.yaml.

Problem-first, date-ordered. Tags are secondary: they exist for filtering,
not for folder structure. `--check` exits non-zero when README.md is stale,
so CI fails instead of letting the index drift from reality.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / "catalog.yaml"
README = ROOT / "README.md"
STATUS_ORDER = {"flagship": 0, "practice": 1}


def load() -> list[dict]:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8")) or {}
    records = data.get("records") or []
    return sorted(
        records,
        key=lambda r: (STATUS_ORDER.get(r.get("status", "practice"), 9), str(r.get("date", "")), r.get("id", "")),
    )


def render(records: list[dict]) -> str:
    flagships = [r for r in records if r.get("status") == "flagship"]
    practice = [r for r in records if r.get("status") != "flagship"]
    all_tags = sorted({t for r in records for t in (r.get("tags") or [])})

    out: list[str] = []
    out.append("# Lab catalogue")
    out.append("")
    out.append("Each entry is a problem I hit, the artifact that answers it, and the command that")
    out.append("proves it. Entries are ordered by date, because the useful signal is not the")
    out.append("technology — it is that the problem was actually closed.")
    out.append("")
    out.append(f"{len(records)} entries · {len(flagships)} flagship · {len(all_tags)} tags")
    out.append("")
    out.append("## Flagship")
    out.append("")
    for r in flagships:
        out.extend(render_record(r, link=True))
    if practice:
        out.append("## Practice and specimens")
        out.append("")
        for r in practice:
            out.extend(render_record(r, link=True))
    out.append("## Tags")
    out.append("")
    for t in all_tags:
        ids = [r["id"] for r in records if t in (r.get("tags") or [])]
        out.append(f"- `{t}` — {', '.join(ids)}")
    out.append("")
    return "\n".join(out)


def render_record(r: dict, link: bool) -> list[str]:
    lines = [f"### {r['id']}  ·  {r.get('date', '')}"]
    lines.append("")
    lines.append(f"**Problem** — {r.get('problem', '')}")
    lines.append("")
    lines.append(f"**Proved** — {r.get('proved', '')}")
    lines.append("")
    verify = r.get("verify", "").strip()
    if verify:
        lines.append(f"**Verify** — `{verify}`")
        lines.append("")
    repo = (r.get("repo") or "").strip()
    if link:
        lines.append(f"**Repo** — {repo if repo else '_local, not published yet_'}")
        lines.append("")
    return lines


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if README.md is stale")
    args = ap.parse_args()

    text = render(load())
    if args.check:
        current = README.read_text(encoding="utf-8") if README.exists() else ""
        if current.strip() != text.strip():
            print("README.md is stale: run `make gen`", file=sys.stderr)
            return 1
        print("catalog is up to date")
        return 0

    README.write_text(text, encoding="utf-8")
    print(f"wrote {README.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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


def load_data() -> dict:
    return yaml.safe_load(CATALOG.read_text(encoding="utf-8")) or {}


def load() -> list[dict]:
    data = load_data()
    records = data.get("records") or []
    return sorted(
        records,
        key=lambda r: (STATUS_ORDER.get(r.get("status", "practice"), 9), _neg_date(r.get("date", "")), r.get("id", "")),
    )


def _neg_date(d: str) -> tuple:
    # newest first inside a status group
    parts = [int(x) for x in str(d).split("-") if x.isdigit()]
    return tuple(-x for x in parts)


def render_figure() -> list[str]:
    """One figure, generated like everything else, so the README stays reproducible."""
    return [
        "## The shape of it",
        "",
        "The figure answers one question: how a reader gets from nineteen repositories to one page.",
        "",
        "![catalog.yaml, a generator, the generated README, and a CI check that fails on drift](docs/figures/catalog-pipeline.png)",
        "",
        "**Figure 1.** One hand-edited file generates everything a reader sees, and the same generator "
        "runs in check mode in CI, so a stale index fails the build instead of quietly describing work "
        "that no longer exists. Source: [`docs/figures/catalog-pipeline.html`](docs/figures/catalog-pipeline.html).",
        "",
    ]


def render_themes(themes: list[dict], records: list[dict]) -> list[str]:
    out: list[str] = ["## What I keep working on", ""]
    out.append("Four recurring problems. Each line is a claim; the entries under it are the evidence.")
    out.append("")
    for t in themes:
        hits = [r for r in records if t.get("id") in (r.get("themes") or [])]
        out.append(f"**{t.get('title', t.get('id'))}** · {len(hits)} — {t.get('claim', '')}")
        out.append("")
        for r in sorted(hits, key=lambda x: str(x.get("date", "")), reverse=True):
            out.append(f"- `{r['id']}` · {r.get('date', '')} · {r.get('proved', '')}")
        if not hits:
            out.append("- _no entry yet_")
        out.append("")
    return out


def render_table(records: list[dict]) -> list[str]:
    out: list[str] = ["## All entries", ""]
    out.append("| id | date | problem | tags |")
    out.append("|---|---|---|---|")
    for r in sorted(records, key=lambda x: str(x.get("date", "")), reverse=True):
        problem = str(r.get("problem", "")).replace("|", "/")
        if len(problem) > 90:
            problem = problem[:87] + "..."
        tags = ", ".join(r.get("tags") or [])
        out.append(f"| `{r['id']}` | {r.get('date', '')} | {problem} | {tags} |")
    out.append("")
    return out


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
    out.append("Entries marked **private** cannot be checked by a reader. They are listed as ongoing")
    out.append("work, not as proof, and they carry no command that pretends otherwise.")
    out.append("")
    out.append(f"{len(records)} entries · {len(flagships)} flagship · {len(all_tags)} tags")
    out.append("")
    out.extend(render_figure())
    out.extend(render_themes(load_data().get("themes") or [], records))
    out.append("## Flagship")
    out.append("")
    for r in flagships:
        out.extend(render_record(r, link=True))
    if practice:
        out.append("## Practice and specimens")
        out.append("")
        for r in practice:
            out.extend(render_record(r, link=True))
    out.extend(render_table(records))
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
    usage = (r.get("usage") or "").strip()
    if usage:
        lines.append(f"**Use** — {usage}")
        lines.append("")
    verify = r.get("verify", "").strip()
    private = (r.get("visibility") or "").strip() == "private"
    if verify and not private:
        lines.append(f"**Verify** — `{verify}`")
        lines.append("")
    elif private:
        lines.append("**Verify** — _not runnable by a reader: the repository is private_")
        lines.append("")
    repo = (r.get("repo") or "").strip()
    if link:
        if repo:
            lines.append(f"**Repo** — {repo}")
        else:
            lines.append("**Repo** — _private, not published: you cannot check this one, only ask me to walk through it_")
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

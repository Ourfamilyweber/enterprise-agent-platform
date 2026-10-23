#!/usr/bin/env python3
"""Assemble canonical harness Markdown into the generated Pages source tree."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def copy_markdown(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    content = source.read_text(encoding="utf-8")
    content = rewrite_directory_links(source, content)
    if source.parts[-3:-1] == (".github", "agents"):
        content = content.replace(".github/skills/", "../skills/")
    if source == ROOT / "AGENTS.md":
        content = content.replace(".github/agents/", "agents/")
    destination.write_text(content, encoding="utf-8")


def rewrite_directory_links(source: Path, content: str) -> str:
    pattern = re.compile(r"\]\(([^)\s]+/)(#[^)]+)?\)")

    def replace(match: re.Match[str]) -> str:
        target, fragment = match.groups()
        if target.startswith(("http:", "https:", "mailto:")):
            return match.group(0)
        resolved = (source.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            return match.group(0)
        if not resolved.is_dir():
            return match.group(0)
        return f"]({target}index.md{fragment or ''})"

    return pattern.sub(replace, content)


def write_folder_index(folder: Path, docs_folder: Path, title: str, plan: str | None = None) -> None:
    docs_folder.mkdir(parents=True, exist_ok=True)
    rows = [f"# {title}", ""]
    if plan:
        rows.extend([f"[Open the phase plan]({plan})", ""])
    rows.extend(["## Documents", ""])
    for path in sorted(folder.rglob("*.md")):
        label = path.stem.replace("-", " ").title()
        relative_path = path.relative_to(folder).as_posix()
        rows.append(f"- [{label}]({relative_path})")
    (docs_folder / "index.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def prepare_getting_started(source: Path, destination: Path) -> None:
    content = source.read_text(encoding="utf-8")
    replacements = {
        "(00-framing/)": "(00-framing/index.md)",
        "(01-preparation/)": "(01-preparation/index.md)",
        "(02-design/)": "(02-design/index.md)",
        "(02-design/domains/)": "(02-design/domains/index.md)",
        "(03-architecture/)": "(03-architecture/index.md)",
        "(04-implementation/)": "(04-implementation/index.md)",
        "(05-sizing/)": "(05-sizing/index.md)",
        "(06-operations/)": "(06-operations/index.md)",
        "(07-presentation/)": "(07-presentation/index.md)",
        "(AGENTS.md)": "(agent-guides/roster-and-collaboration.md)",
    }
    for old, new in replacements.items():
        content = content.replace(old, new)
    content = re.sub(
        r"\[([^\]]+)\]\([^)]*architecture-harness\.json[^)]*\)",
        "`architecture-harness.json`",
        content,
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def main() -> None:
    manifest = json.loads((ROOT / "architecture-harness.json").read_text(encoding="utf-8"))
    DOCS.mkdir(exist_ok=True)

    for phase in manifest["phases"]:
        folder = ROOT / phase["folder"]
        for source in folder.rglob("*.md"):
            copy_markdown(source, DOCS / source.relative_to(ROOT))
        plan_name = Path(phase["plan"]).name
        write_folder_index(
            folder,
            DOCS / phase["folder"],
            phase["name"].replace("-", " ").title(),
            plan_name,
        )

    prepare_getting_started(ROOT / "README.md", DOCS / "getting-started.md")
    copy_markdown(ROOT / "AGENTS.md", DOCS / "agent-guides" / "roster-and-collaboration.md")
    reference = DOCS / "reference"
    reference.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "architecture-harness.json", reference / "architecture-harness.json")

    agents = ROOT / ".github" / "agents"
    skills = ROOT / ".github" / "skills"
    for source in agents.rglob("*.md"):
        copy_markdown(source, DOCS / "agent-guides" / "agents" / source.relative_to(agents))
    for source in skills.rglob("*.md"):
        copy_markdown(source, DOCS / "agent-guides" / "skills" / source.relative_to(skills))
    write_folder_index(agents, DOCS / "agent-guides" / "agents", "Agent Guides")
    write_folder_index(skills, DOCS / "agent-guides" / "skills", "Portable Skills")
    write_folder_index(ROOT / "02-design" / "domains", DOCS / "02-design" / "domains", "Design Domains")

    phase_rows = []
    for phase in manifest["phases"]:
        plan_link = phase["plan"]
        phase_rows.append(
            f"| [{phase['name'].replace('-', ' ').title()}]({plan_link}) "
            f"| {', '.join(phase['mayStartAfter']) or 'Project input'} "
            f"| {', '.join(phase['exitGateRequires']) or 'None'} "
            f"| {phase['exitGate']} |"
        )

    landing = "\n".join(
        [
            "# Enterprise Architecture Harness",
            "",
            "A source-controlled, agent-assisted method for moving from framing to an evidence-backed architecture, implementation handoff, sizing model, operating model, and decision package.",
            "",
            "The phase artifacts are canonical. This site adds navigation and rendering; it does not replace source Markdown or record approvals.",
            "",
            "## Lifecycle",
            "",
            "| Phase | May start after | Exit gate requires | Exit gate |",
            "|---|---|---|---|",
            *phase_rows,
            "",
            "## Start here",
            "",
            "- [Getting started](getting-started.md)",
            "- [Framing scenario](00-framing/03-scenario.md)",
            "- [Governance](01-preparation/15-governance.md)",
            "- [Change-impact register](01-preparation/16-change-impact-register.md)",
            "- [Gate register](01-preparation/17-gate-register.md)",
            "- [Architecture-validated scenario](07-presentation/76-validated-scenario.md)",
            "- [Agent roster and collaboration](agent-guides/roster-and-collaboration.md)",
            "",
            "## Working rules",
            "",
            "- A readiness recommendation is not a gate decision.",
            "- A designed control is not implementation or operational evidence.",
            "- Product choices require an accepted need, comparison, and decision authority.",
            "- Changes replay only affected work; the change register preserves the rationale.",
            "",
            "## Reference",
            "",
            "The machine-readable `architecture-harness.json` manifest defines phase dependencies, gates, identifiers, and agent policy.",
        ]
    )
    (DOCS / "index.md").write_text(landing + "\n", encoding="utf-8")
    manifest_rows = [
        "# Harness Manifest",
        "",
        f"Schema version: `{manifest['schemaVersion']}`",
        "",
        "| Phase | Folder | Start condition | Exit gate |",
        "|---|---|---|---|",
    ]
    for phase in manifest["phases"]:
        manifest_rows.append(
            f"| [{phase['name'].replace('-', ' ').title()}](../{phase['plan']}) "
            f"| `{phase['folder']}` "
            f"| {', '.join(phase['mayStartAfter']) or 'Project input'} "
            f"| {phase['exitGate']} |"
        )
    (DOCS / "reference" / "manifest.md").write_text("\n".join(manifest_rows) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
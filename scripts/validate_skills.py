"""Validate portable skill metadata and repository-local Markdown links."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root):
    errors = []
    skills = sorted(root.glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found")
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{path.name}: invalid YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.name}: frontmatter must be a mapping")
            continue
        name = data.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != path.parent.name:
            errors.append(f"{path.parent.name}: invalid name")
        description = data.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{path.parent.name}: invalid description")
        allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
        if set(data) - allowed:
            errors.append(f"{path.parent.name}: unsupported metadata fields")
        metadata = data.get("metadata", {})
        if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
            errors.append(f"{path.parent.name}: metadata must map strings to strings")
        if not text[match.end():].strip():
            errors.append(f"{path.parent.name}: empty instructions")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            resolved = (path.parent / local).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"{path.relative_to(root)}: invalid local link {target}")
    return skills, errors


if __name__ == "__main__":
    skills, errors = validate(ROOT)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print(f"Validated {len(skills)} skills and local Markdown links")

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "contest_profile.json"
REQUIRED_TEMPLATES = {
    "problem.md",
    "data-audit.md",
    "experiment.md",
    "decision.md",
    "risk-register.md",
    "debate-card.md",
}
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
}
SKIP_PARTS = {".git", ".venv", "__pycache__", "node_modules"}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidate_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not any(part in SKIP_PARTS for part in path.parts)
    )


def main() -> int:
    failures: list[str] = []
    if sys.version_info < (3, 11):
        failures.append(f"Python 3.11+ required; found {sys.version.split()[0]}")

    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    if profile.get("schema_version") != "cofathon-contest-profile-v1":
        failures.append("unexpected contest profile schema")
    phase_total = sum(int(item["minutes"]) for item in profile.get("phases", []))
    duration_minutes = profile.get("duration_minutes")
    if phase_total != duration_minutes or phase_total != 225:
        failures.append(f"phase total must be 225; found {phase_total}")
    if profile.get("post_submission_question_minutes") != 3:
        failures.append("post-submission question budget must be 3 minutes")
    if profile.get("extension_assumed") is not False:
        failures.append("extension must not be assumed in the base plan")
    if profile.get("max_active_heavy_workers") != 1:
        failures.append("contest profile must keep one active heavy worker")
    if profile.get("bundle_ready_minute", 999) > duration_minutes - 10:
        failures.append("bundle must be ready with at least 10 minutes remaining")

    template_dir = ROOT / "templates"
    observed_templates = {path.name for path in template_dir.glob("*.md")}
    missing_templates = sorted(REQUIRED_TEMPLATES - observed_templates)
    if missing_templates:
        failures.append("missing templates: " + ", ".join(missing_templates))

    findings: list[str] = []
    for path in candidate_files():
        if path.suffix.lower() in {".zip", ".pyc", ".png", ".jpg", ".jpeg"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{name}:{path.relative_to(ROOT).as_posix()}")
    if findings:
        failures.append("potential secret material: " + ", ".join(findings))

    report = {
        "schema_version": "cofathon-preflight-v1",
        "status": "PASS" if not failures else "FAIL",
        "python": sys.version.split()[0],
        "platform": sys.platform,
        "phase_total_minutes": phase_total,
        "file_count": len(candidate_files()),
        "profile_sha256": file_hash(PROFILE),
        "failures": failures,
        "environment_secret_values_read": False,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

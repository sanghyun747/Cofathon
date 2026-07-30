from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_MAP = {
    ROOT / "templates" / "problem.md": Path("problem.md"),
    ROOT / "templates" / "data-audit.md": Path("data-audit.md"),
    ROOT / "templates" / "experiment.md": Path("experiment-template.md"),
    ROOT / "templates" / "decision.md": Path("decisions.md"),
    ROOT / "templates" / "risk-register.md": Path("risks.md"),
    ROOT / "templates" / "debate-card.md": Path("debate-card.md"),
    ROOT / "task_contract.template.json": Path("task-contract.json"),
    ROOT / "run-receipt.template.json": Path("run-receipt.json"),
}
DIRECTORIES = (
    "baseline",
    "candidate",
    "champion",
    "test-results",
    "submission",
)


def initialize(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (output / directory).mkdir(exist_ok=True)
    for source, relative in TEMPLATE_MAP.items():
        destination = output / relative
        if not destination.exists():
            shutil.copyfile(source, destination)
    experiments = output / "experiments.jsonl"
    if not experiments.exists():
        experiments.write_text("", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output).resolve()
    initialize(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import os
from pathlib import Path

FINAL_LINE = "That WAS a shortcut - you have arrived eleven minutes early, just in a lake, behind a stranger's wedding convoy, which I am officially calling a scenic route."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)

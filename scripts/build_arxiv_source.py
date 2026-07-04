from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "paper18_submission_source"
OUT = ROOT / "arxiv_submission_source.zip"


def include(path: Path) -> bool:
    if path.name == "main.pdf":
        return False
    if path.suffix in {".aux", ".bbl", ".bcf", ".blg", ".log", ".out", ".run.xml", ".toc"}:
        return False
    return True


def main() -> None:
    if OUT.exists():
        OUT.unlink()
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in SRC.rglob("*"):
            if path.is_file() and include(path):
                zf.write(path, path.relative_to(SRC))
    print(f"WROTE {OUT}")


if __name__ == "__main__":
    main()

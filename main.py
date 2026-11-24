"""A single emoji, nothing else, standing in for the trip of my dreams.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "🏝️"


def main():
    assert 1 <= len(TEXT) <= 8, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

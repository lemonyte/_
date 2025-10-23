import sys
from pathlib import Path

from underscores._ import _


def cmd() -> None:
    code = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
    sys.stdout.write(_(code))
    sys.stdout.flush()


if __name__ == "__main__":
    cmd()

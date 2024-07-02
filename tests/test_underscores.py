from __future__ import annotations

import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path
from typing import Generator, NamedTuple

import pytest


class CodePair(NamedTuple):
    decoded: str
    encoded: str


TEST_DATA_FILE_PATHS = (("decoded.py", "encoded.py"),)
TEST_DATA = tuple(
    CodePair(*((Path(__file__).parent / "code" / path).read_text(encoding="utf-8") for path in paths))
    for paths in TEST_DATA_FILE_PATHS
)


@pytest.fixture()
def _install_pth_file() -> Generator[None, None, None]:
    """Install the `_.pth` file in the site-packages directory to make the execute tests work."""
    src_pth_file = Path(__file__).parent.parent / "underscores" / "_.pth"
    site_packages = sysconfig.get_path("purelib")
    shutil.copy(src_pth_file, Path(sys.prefix) / site_packages)
    installed_pth_file = Path(sys.prefix) / site_packages / "_.pth"
    assert installed_pth_file.exists()
    yield
    installed_pth_file.unlink()


@pytest.mark.usefixtures("_install_pth_file")
@pytest.mark.parametrize(("file_pair"), TEST_DATA_FILE_PATHS)
def test_execute(file_pair: tuple[str, str]) -> None:
    processes = tuple(
        subprocess.run(
            (sys.executable, "-X", "utf8", Path(__file__).parent / "code" / file_path),
            capture_output=True,
            check=False,
            encoding="utf-8",
        )
        for file_path in file_pair
    )
    assert processes[0].stdout == processes[1].stdout, f"{processes[0].stderr}\n\n{processes[1].stderr}"


@pytest.mark.parametrize(("code_pair"), TEST_DATA)
def test_encode(code_pair: CodePair) -> None:
    assert code_pair.decoded.encode("_").decode("utf-8") == code_pair.encoded


@pytest.mark.parametrize(("code_pair"), TEST_DATA)
def test_decode(code_pair: CodePair) -> None:
    assert code_pair.encoded.encode("utf-8").decode("_").lstrip("\n") == code_pair.decoded

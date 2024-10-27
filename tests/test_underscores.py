from __future__ import annotations

import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

import pytest

import underscores

if TYPE_CHECKING:
    from collections.abc import Generator


class CodePair(NamedTuple):
    decoded: str
    encoded: str


class FilePair(NamedTuple):
    decoded: Path
    encoded: Path


SRC_DIR = Path(__file__).parent.parent / "src"
TEST_CODE_DIR = Path(__file__).parent / "code"
TEST_FILES = (
    FilePair(
        decoded=TEST_CODE_DIR / "decoded.py",
        encoded=TEST_CODE_DIR / "encoded.py",
    ),
)
TEST_CODE = tuple(CodePair(*(file.read_text(encoding="utf-8") for file in file_pair)) for file_pair in TEST_FILES)


@pytest.fixture
def install_pth_file() -> Generator[None, None, None]:
    """Install the `_.pth` file in the site-packages directory to make the execute tests work."""
    src_pth_file = SRC_DIR / "underscores" / "_.pth"
    site_packages = sysconfig.get_path("purelib")
    shutil.copy(src_pth_file, Path(sys.prefix) / site_packages)
    installed_pth_file = Path(sys.prefix) / site_packages / "_.pth"
    assert installed_pth_file.exists()
    yield
    installed_pth_file.unlink()


@pytest.mark.usefixtures("install_pth_file")
@pytest.mark.parametrize(("file_pair"), TEST_FILES)
def test_execute(file_pair: FilePair) -> None:
    args = (sys.executable, "-X", "utf8")
    decoded_process = subprocess.run(
        (*args, file_pair.decoded),
        check=False,
        capture_output=True,
        encoding="utf-8",
    )
    encoded_process = subprocess.run(
        (*args, file_pair.encoded),
        check=False,
        capture_output=True,
        encoding="utf-8",
    )
    assert decoded_process.stdout == encoded_process.stdout, f"{decoded_process.stderr}\n\n{encoded_process.stderr}"


@pytest.mark.parametrize(("code_pair"), TEST_CODE)
def test_encode(code_pair: CodePair) -> None:
    assert code_pair.decoded.encode("_").decode("utf-8") == code_pair.encoded


@pytest.mark.parametrize(("code_pair"), TEST_CODE)
def test_decode(code_pair: CodePair) -> None:
    assert code_pair.encoded.encode("utf-8").decode("_").lstrip("\n") == code_pair.decoded


@pytest.mark.parametrize(("code_pair"), TEST_CODE)
def test_underscores_function(code_pair: CodePair) -> None:
    assert underscores._(code_pair.decoded) == code_pair.encoded

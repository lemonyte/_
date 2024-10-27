from __future__ import annotations

import itertools
from codecs import CodecInfo, register
from encodings import utf_8
from io import StringIO
from pathlib import Path
from tokenize import NAME, NL, generate_tokens
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import ReadableBuffer

__all__ = ("_",)

NUM_WIDTH = 4
MAX_LINE_LENGTH = 80


def decimal_to_base(num: int, /, *, base: int) -> str:
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        num, r = divmod(num, base)
        digits.append(str(r))
    return "".join(digits[::-1])


def _(src: str, /) -> str:
    """`_`-ify source code.

    Each byte in the source string is converted into a base-6 representation,
    then into a group of underscore sequences. The lengths of the underscore
    sequences represent the digits of the base-6 number plus one.
    Example: `"A"` -> `65` -> `"0145"` -> `"1256"` -> `"_ __ _____ ______"`
    """
    underscores = (
        "_" * (int(digit) + 1)
        for digit in itertools.chain.from_iterable(
            tuple(decimal_to_base(char, base=6).zfill(NUM_WIDTH)) for char in src.encode("utf-8")
        )
    )
    lines = []
    for underscore in underscores:
        if not lines or len(lines[-1]) + len(underscore) + 1 > MAX_LINE_LENGTH:
            lines.append("")
        else:
            lines[-1] += " "
        lines[-1] += underscore
    return "\n".join(("# coding: _", *lines, ""))


def encode(input: str, errors: str = "strict", /) -> tuple[bytes, int]:
    return utf_8.encode(_(input), errors)


def decode(input: ReadableBuffer, errors: str = "strict") -> tuple[str, int]:
    decoded, size = utf_8.decode(input, errors)
    chars = []
    underscores = []
    for token in generate_tokens(StringIO(decoded).readline):
        if token.type == NAME and set(token.string) == {"_"}:
            underscores.append(token.string)
            if len(underscores) == NUM_WIDTH:
                # Base-6 representation of a character as a string.
                num_string = "".join([str(len(string) - 1) for string in underscores])
                chars.append(int(num_string, base=6))
                underscores = []
        # Leading newline is required for Python to execute the decoded code.
        if token.type == NL:
            chars.append(ord("\n"))
    code = bytes(chars).decode("utf-8")
    return code, size


class IncrementalDecoder(utf_8.IncrementalDecoder):
    def decode(self, input: ReadableBuffer, final: bool = False) -> str:  # noqa: FBT001 FBT002
        self.buffer += input
        if final:
            decoded, _ = decode(self.buffer)
            self.buffer = b""
            return decoded
        return ""


@register
def search_function(encoding_name: str) -> CodecInfo | None:
    # Python 3.9 and later remove underscores and dashes from encoding names.
    if encoding_name in ("_", ""):
        return CodecInfo(
            name="_",
            encode=encode,
            decode=decode,
            incrementaldecoder=IncrementalDecoder,
        )
    return None


if __name__ == "__main__":
    print(Path(__file__).read_text(encoding="utf-8").encode("_").decode("utf-8"))

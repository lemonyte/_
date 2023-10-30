import os
import sys
import sysconfig
from pathlib import Path

from setuptools import setup

import underscores

SITE_PACKAGES = sysconfig.get_path("purelib").split(sys.prefix + os.sep)[1]

setup(
    name="underscores",
    version=underscores.__version__,
    description="_ allows you to write Python code using only _.",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/lemonyte/_",
    author="Lemonyte",
    python_requires=">=3.8",
    packages=["underscores"],
    data_files=[(SITE_PACKAGES, ["underscores/_.pth"])],
    keywords=["_", "underscore", "encoding", "joke"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)

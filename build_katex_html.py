# Copyright 2023 Jesse Stricker.
# SPDX-License-Identifier: Apache-2.0

from io import BufferedWriter
from os import makedirs
from pathlib import Path
from shutil import copyfileobj
from typing import Final
from urllib.request import urlopen

VERSION: Final = "0.16.8"
SCRIPT_FILE_NAME: Final = "katex.min.js"
OUTPUT_FILE_NAME: Final = "katex.html"


def build_url(file_name: str) -> str:
    """Build an URL to the KaTeX asset file named ``file_name``."""
    return f"https://cdn.jsdelivr.net/npm/katex@{VERSION}/dist/{file_name}"


def download_to_end_of(file: BufferedWriter, url: str) -> None:
    """Download the resource located at ``url`` and append it to ``file``."""
    with urlopen(url) as response:
        copyfileobj(response, file)


def main() -> None:
    output_file_path = Path(__file__).parent / ".cargo" / OUTPUT_FILE_NAME
    makedirs(output_file_path.parent, exist_ok=True)

    with output_file_path.open("wb") as output_file:
        output_file.write(f"<!-- KaTeX v{VERSION} -->\n".encode())
        output_file.write(b"<script>\n")
        download_to_end_of(output_file, build_url(SCRIPT_FILE_NAME))
        output_file.write(b"\n</script>\n")


if __name__ == "__main__":
    main()

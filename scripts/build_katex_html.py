# Copyright 2023 Jesse Stricker.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from io import BufferedWriter
from os import makedirs
from pathlib import Path
from shutil import copyfileobj
from typing import Final
from urllib.request import urlopen

SCRIPT_FILE_NAME: Final = "katex.min.js"
OUTPUT_FILE_NAME: Final = "katex.html"


def _build_url(file_name: str, version: str) -> str:
    """Build an URL to the KaTeX asset file named ``file_name``."""
    return f"https://cdn.jsdelivr.net/npm/katex@{version}/dist/{file_name}"


def _download_to_end_of(file: BufferedWriter, url: str) -> None:
    """Download the resource located at ``url`` and append it to ``file``."""
    with urlopen(url) as response:
        copyfileobj(response, file)


def build_katex_html(version: str) -> None:
    output_file_path = Path(__file__).parent / ".cargo" / OUTPUT_FILE_NAME
    makedirs(output_file_path.parent, exist_ok=True)

    with output_file_path.open("wb") as output_file:
        output_file.write(f"<!-- KaTeX v{version} -->\n".encode())
        output_file.write(b"<script>\n")
        _download_to_end_of(output_file, _build_url(SCRIPT_FILE_NAME, version))
        output_file.write(b"\n</script>\n")


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("version", help="The KaTeX version")
    args = parser.parse_args()
    build_katex_html(args.version)


if __name__ == "__main__":
    main()

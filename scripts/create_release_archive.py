# Copyright 2023 Jesse Stricker.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser
from pathlib import Path
from shutil import make_archive
from typing import Final

FORMATS: Final = ["zip", "gztar"]
PROJECT_DIR: Final = Path(__file__).parent.parent


def create_release_archives(version: str) -> None:
    archive_base_path = PROJECT_DIR / f"rustdoc-katex-v{version}"
    contents_base_dir = PROJECT_DIR / ".cargo"

    for format in FORMATS:
        make_archive(
            str(archive_base_path),
            format,
            PROJECT_DIR,
            contents_base_dir.relative_to(PROJECT_DIR),
        )


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("version", help="The rustdoc-katex version")
    args = parser.parse_args()
    create_release_archives(args.version)


if __name__ == "__main__":
    main()

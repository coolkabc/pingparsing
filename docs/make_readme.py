#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import sys

from path import Path
from readmemaker import ReadmeMaker


PROJECT_NAME = "pingparsing"
OUTPUT_DIR = ".."


def write_examples(maker):
    maker.set_indent_level(0)

    usage_root = Path("pages").joinpath("usage")

    maker.write_file(usage_root.joinpath("cli_usage.txt"))
    maker.write_file(usage_root.joinpath("cli_help.txt"))
    maker.write_file(usage_root.joinpath("library.rst"))


def main():
    maker = ReadmeMaker(
        PROJECT_NAME,
        OUTPUT_DIR,
        is_make_toc=True,
        project_url="https://github.com/thombashi/{}".format(PROJECT_NAME),
    )
    maker.examples_dir_name = "usage"

    maker.write_chapter("Summary")
    maker.write_introduction_file("summary.txt")
    maker.write_introduction_file("badges.txt")

    write_examples(maker)

    maker.write_file(maker.doc_page_root_dir_path.joinpath("installation.rst"))
    maker.write_introduction_file("supported_environment.txt")
    maker.write_file(maker.doc_page_root_dir_path.joinpath("introduction/premise.txt"))

    maker.set_indent_level(0)
    maker.write_chapter("Documentation")
    maker.write_lines(["https://{:s}.rtfd.io/".format(PROJECT_NAME)])

    return 0


if __name__ == "__main__":
    sys.exit(main())

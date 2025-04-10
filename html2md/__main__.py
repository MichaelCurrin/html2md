import argparse
from pathlib import Path
import sys
from typing import Optional

from markdownify import ATX
from markdownify import markdownify as md

BULLETS = "-*+"


def _get_content(input_path_str: str) -> str:
    """
    Read input from given file.
    """

    input_path = Path(input_path_str)
    assert input_path.exists(), f"Unable to read file at path: {input_path}"

    with open(input_path, encoding="utf-8") as f_in:
        return f_in.read().strip()

def convert_input(html_value: str) -> md:


    return


def main():
    """
    Main command-line entry-point.
    """
    parser = argparse.ArgumentParser(description="Convert HTML content to Markdown.")
    parser.add_argument(
        "--file",
        "-f",
        metavar="PATH",
        type=str,
        required=False,
        help="Path to input file.",
    )
    parser.add_argument(
        "--value",
        "-v",
        metavar="HTML",
        type=str,
        required=False,
        help="HTML input value.",
    )
    args = parser.parse_args()
    print(args)
    if not args.file and not args.value:
        raise ValueError("Must provide one of the input path or HTML value.")

    html_value = _get_content(args.file) if args.file else args.value
    result = md(html_value, heading_style=ATX, bullets=BULLETS)
    print(result)


if __name__ == "__main__":
    main()

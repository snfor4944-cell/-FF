"""Command-line entry point for the Sniffle project."""

from __future__ import annotations

import argparse

from .core import count_chars, count_words, normalize_whitespace, reverse_text, slugify


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sniffle text utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    normalize = subparsers.add_parser("normalize", help="Trim and normalize whitespace")
    normalize.add_argument("text", help="Text to normalize")

    count = subparsers.add_parser("count", help="Count words in text")
    count.add_argument("text", help="Text to count")

    upper = subparsers.add_parser("upper", help="Convert text to uppercase")
    upper.add_argument("text")

    lower = subparsers.add_parser("lower", help="Convert text to lowercase")
    lower.add_argument("text")

    reverse = subparsers.add_parser("reverse", help="Reverse text")
    reverse.add_argument("text")

    slug = subparsers.add_parser("slug", help="Create a slug from text")
    slug.add_argument("text")

    stats = subparsers.add_parser("stats", help="Display basics statistics for text")
    stats.add_argument("text")

    return parser


def _handle_stats(text: str) -> str:
    chars = count_chars(text, include_spaces=True)
    letters = count_chars(text)
    words = count_words(text)
    return f"chars={chars} chars_no_spaces={letters} words={words}"


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "normalize":
        print(normalize_whitespace(args.text))
    elif args.command == "count":
        print(count_words(args.text))
    elif args.command == "upper":
        print(args.text.upper())
    elif args.command == "lower":
        print(args.text.lower())
    elif args.command == "reverse":
        print(reverse_text(args.text))
    elif args.command == "slug":
        print(slugify(args.text))
    elif args.command == "stats":
        print(_handle_stats(args.text))
    else:
        parser.error(f"Unknown command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

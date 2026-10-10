"""Core helpers for a compact text-utility CLI."""

from __future__ import annotations

import re


def normalize_whitespace(text: str) -> str:
    """Collapse repeated whitespace and trim leading/trailing spaces."""
    if text is None:
        raise TypeError("text must not be None")
    return " ".join(str(text).split())


def count_words(text: str) -> int:
    """Return the number of words in a string."""
    normalized = normalize_whitespace(text)
    return len(normalized.split()) if normalized else 0


def count_chars(text: str, include_spaces: bool = False) -> int:
    """Return the character count in a string."""
    if text is None:
        raise TypeError("text must not be None")
    value = str(text)
    if include_spaces:
        return len(value)
    return len(value.replace(" ", ""))


def reverse_text(text: str) -> str:
    """Reverse a string while preserving whitespace exactly."""
    if text is None:
        raise TypeError("text must not be None")
    return str(text)[::-1]


def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug."""
    normalized = normalize_whitespace(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized)
    return slug.strip("-")

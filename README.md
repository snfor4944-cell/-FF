# Sniffle

Sniffle is a small text-focused CLI utility for normalizing, counting, and transforming text.

## Features

- Normalize whitespace
- Count words and characters
- Convert to uppercase/lowercase/title case
- Slugify text for filenames or URLs
- Reverse text
- Print simple text statistics

## Quick start

```bash
pip install -e .
sniffle count "hello world"
sniffle slug "Hello, World!"

# or without PATH configuration:
python -m sniffle count "hello world"
```

## Commands

```bash
sniffle normalize "Hello   world"
sniffle count "one two three"
sniffle upper "hello"
sniffle lower "HELLO"
sniffle reverse "hello"
sniffle slug "Hello, World!"
sniffle stats "Hello world"
```

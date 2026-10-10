from sniffle.core import count_chars, count_words, normalize_whitespace, reverse_text, slugify


def test_normalize_whitespace():
    assert normalize_whitespace("  Hello   world\n") == "Hello world"


def test_count_words():
    assert count_words("one two   three") == 3
    assert count_words("   ") == 0


def test_count_chars():
    assert count_chars("a b c", include_spaces=False) == 3
    assert count_chars("a b c", include_spaces=True) == 5


def test_reverse_text():
    assert reverse_text("hello") == "olleh"


def test_slugify():
    assert slugify("Hello, World!") == "hello-world"

def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def count_lines(text):
    return len(text.splitlines()) if text else 0

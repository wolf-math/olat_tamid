def bold_first_word(text):
    words = text.split()
    if words:
        words[0] = '**' + words[0] + '**'
    return ' '.join(words)


def bold(text):
    stripped = text.strip()
    return f"**{stripped}**"
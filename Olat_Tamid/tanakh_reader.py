import json, sys

def verse(book, chapter, verse):
    chapter_index = int(chapter) - 1
    verse_index = int(verse) - 1
    
    with open(f"Tanakh_niqqud.json", "r") as text:
        data = json.load(text)

    if book not in data or chapter_index >= len(data[book]['text']) or verse_index >= len(data[book]['text'][chapter_index]):
        return "Oops something went wrong"
        
    return (f"{book} {chapter}:{verse}", data[book]['text'][chapter_index][verse_index])


def chapter(book, chapter):
    chapter_index = int(chapter) - 1
    
    with open(f"Tanakh_niqqud.json", "r") as text:
        data = json.load(text)

    if book not in data or chapter_index >= len(data[book]['text']):
        return "Oops something went wrong"

    chapter_list = data[book]['text'][chapter_index]
    chapter_string = ' '.join(chapter_list)

    return (f"{book} {chapter}", chapter_string)


def verses(book, chapter, verse, count):
    chapter_index = int(chapter) - 1
    verse_index = int(verse) - 1

    with open("Tanakh_niqqud.json", "r") as text:
        data = json.load(text)

    if book not in data or chapter_index >= len(data[book]['text']) or verse_index >= len(data[book]['text'][chapter_index]):
        return "Oops something went wrong"

    verses_list = data[book]['text'][chapter_index][verse_index: verse_index + count]
    verses_string = ' '.join(verses_list)
    
    return (f"{book} {chapter}:{verse} - {verse + count - 1}", verses_string)

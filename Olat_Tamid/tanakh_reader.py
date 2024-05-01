import json, sys, os

module_dir = os.path.dirname(__file__)
tanakh = os.path.join(module_dir, 'Tanakh_niqqud.json')

def verse(book, chapter, verse):
    chapter_index = int(chapter) - 1
    verse_index = int(verse) - 1
    
    with open(tanakh, "r") as text:
        data = json.load(text)

    if book not in data or chapter_index >= len(data[book]['text']) or verse_index >= len(data[book]['text'][chapter_index]):
        return "Oops something went wrong"
        
    return (f"{book} {chapter}:{verse}", data[book]['text'][chapter_index][verse_index])


def chapter(book, chapter):
    chapter_index = int(chapter) - 1
    
    with open(tanakh, "r") as text:
        data = json.load(text)

    if book not in data or chapter_index >= len(data[book]['text']):
        return "Oops something went wrong"

    chapter_list = data[book]['text'][chapter_index]
    chapter_string = ' '.join(chapter_list)

    return (f"{book} {chapter}", chapter_string)


def verses(book, chapter, start, stop):
    chapter_index = int(chapter) - 1
    start_index = int(start) - 1
    stop_index = int(stop) - 1

    with open(tanakh, "r") as text:
        data = json.load(text)

    if book not in data or chapter_index >= len(data[book]['text']) or start_index >= len(data[book]['text'][chapter_index]):
        return "Oops something went wrong"

    verses_list = data[book]['text'][chapter_index][start_index: stop_index + 1]
    verses_string = ' '.join(verses_list)
    
    return (f"{book} {chapter}:{start} - {stop}", verses_string)

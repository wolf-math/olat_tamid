import json, sys

def tanakh_reader(section, book, chapter=None, verse=None):
    with open(f"Tanakh_niqqud.json", "r") as text:
        data = json.load(text)
        # print(data['torah']['genesis']['text'][0][0])
        if verse:
            return data[section][book]['text'][chapter][verse]
        elif chapter:
            return data[section][book]['text'][chapter]
        else:
            return data[section][book]['text']

if __name__ == '__main__':
    verse = sys.argv[4] if len(sys.argv) > 4 else None
    chapter = sys.argv[3] if len(sys.argv) > 3 else None
    book = sys.argv[2] if len(sys.argv) > 2 else None
    section = sys.argv[1] if len(sys.argv) > 1 else None
    # print(verse, chapter, book, section)
    tanakh_reader(section, book, chapter, verse)
    
    
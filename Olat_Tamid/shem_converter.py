aleph_bet = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ך','ל','מ','ם',
             'נ','ן','ס','ע','פ','ף','צ','ק','ר','ש','ת','װ','ױ','ײ','יִ',
             'ﬡ','ﬢ','ﬣ','ﬤ','ﬥ','ﬦ','ﬧ','ﬨ','שׁ','שׂ','שּׁ','שּׂ','אַ','אָ',
             'גּ','דּ','הּ','וּ','זּ','טּ','יּ','ךּ','כּ','לּ','מּ','נּ','סּ','ףּ',
             'פּ','צּ','שּ','תּ','וֹ','בֿ','כֿ','פֿ','ﭏ']

cantellation_marks = ['֑','֒','֓','֔','֕','֖','֗','֘','֙','֚','֛','֜',
             '֝','֞','֠','֡','֢','֣','֤','֥','֦','֧','֨','֩','֪','֫','֬','֭','֯','׃']

vowels = ['ְ','ֱ','ֲ','ֳ','ִ','ֵ','ֶ','ַ','ָ','ֹ','ֺ','ֻ','ּ','ֽ','־','ֿ','ׁ','ׂ','ׄ','ׅ']

shem = 'יהוה'

## Strips vowels and cantelation marks from words
def nonalpha_remover(word):
    no_cant_word = ''
    for letter in word:
        if letter.isalpha() == True:
            no_cant_word = no_cant_word + letter
    return no_cant_word

## Converts Shem-Havaya to double-yud while preserving cantelation marks
def shem_converter(word):
    prefix = ''
    if word[0] != aleph_bet[9]:
        prefix = prefix + word[0]
        if word[1].isalpha() == False:
            prefix = prefix + word[1]
            if word[2].isalpha() == False:
                prefix = prefix + word[2]
    no_prefix_word = word[len(prefix):]

    if len(prefix) > 0:
        yud1 = aleph_bet[9]
    else:
        yud1 = aleph_bet[9]+vowels[0]

    yud2 = aleph_bet[9]+vowels[8]

    cant_marks = []

    for character in no_prefix_word:
        if character in cantellation_marks:
            cant_marks.append(character)
    if len(cant_marks) == 0:
        new_shem = prefix + yud1 + yud2
    elif len(cant_marks) == 1:
        new_shem = prefix + yud1 + yud2 + cant_marks[0]
    elif len(cant_marks) == 2:
        new_shem = prefix + yud1 + cant_marks[0] + yud2 + cant_marks[1]

    return new_shem

## Creates new paragraph with double-yud in place of Shem Havaya

def double_yud(paragraph):
    paragraph = str.replace(paragraph, '־', ' ־ ')
    par_list = paragraph.split()
    for word in par_list:
        index = par_list.index(word)
        if shem in nonalpha_remover(word):
            double_yud = shem_converter(word)
            par_list[index] = double_yud

    new_par = ' '.join(par_list)
    new_par = str.replace(new_par, ' ־ ','־')
    new_par = str.replace(new_par, '׃', '׃ \n')
    return(new_par)


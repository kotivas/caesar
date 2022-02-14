#!/usr/bin/python3
#by kotivas

lang = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ],
        ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 
        'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
        'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 
        'ы', 'ь', 'э', 'ю', 'я']]

in_lang = int(input("Choose an alphabet \n[0] English \n[1] Russian \n:"))
ind = input("\nSpecify an indent\nUse opposite numbers to decrypt\nUse [?] if indent is unknown\n:")
txt = input("\nText to encrypt\n:").lower()

def encrypt(lang, ind, txt):
    result = ''
    for i in range(0, len(txt)):
        if txt[i] not in lang:
                result += txt[i]
                continue

        sym = lang.index(txt[i]) + ind

        if sym >= len(lang):
            sym = sym - len(lang)
        result += lang[sym]
    return result

if ind=='?':
    print("\nOutput text:")
    for i in range(0, len(lang[in_lang])):
        print("Indent -{0}: {1}".format(i, encrypt(lang[in_lang], i * -1, txt)))

else:
    print("\nOutput text: {}".format(encrypt(lang[in_lang], int(ind), txt)))


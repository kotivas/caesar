#!/usr/bin/python3
#by kotivas

# добавления языка для шифрования:
# добавьте алфавит желаемого языка в массив alphabets[8]
# и запишите в массив languages[8] сокр. названия языка (примеры: en, ru, uk)
# так же, добавьте полную расшифровку вашего языка, в список languages в caesar-ui.py

languages = ['en', 'ru']

alphabets = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ],
            ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 
            'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
            'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 
            'ы', 'ь', 'э', 'ю', 'я']]

def encrypt(language, indent, text): # главная (и единственная) функция шифрования/дешифрования
    result = '' # создание пременной для итогового результата
    language = alphabets[languages.index(language)]
    for i in range(0, len(text)):
        if text[i] not in language: # если символа нету в алфавите, то символ записывается в резльтат и пропускается 1 проход цикла
                result += text[i]
                continue
        pos = language.index(text[i]) + indent # вычисляется положение шифрованого символа относительно алфавита
        if pos >= len(language): # если положение шифрованого символа вышло за пределы алфавита
            pos = pos - len(language) # отнимается длина алфавита от положения символа
        result += language[pos] # в итоговую переменную записывается символ
    return result # возвращение зашифрованого/дешифрованого текста


if __name__ == "__main__":

    # получение от пользователя параметров (язык, отступ, текст)
    # если отступ неизвестен '?', цикл выполняется *длина алфавита* раз, и выводит все проходы
    # если отступ известен, функция вызывается 1 раз

    language = input("Choose an alphabet \n " + str(languages) + " \n:").lower() # получение языка
    indent = input("\nSpecify an indent\nUse opposite numbers to decrypt\nUse [?] if indent is unknown\n:") # получение отступа
    text = input("\nText to encrypt\n:").lower() #получения теста для шифрования/дешифрования

    if indent=='?': # цикл если отступ неизвестен
        print("\nOutput text:")
        for i in range(0, len(alphabets[language])):
            print("Indent -{0}: {1}".format(i, language, i * -1, text)) #вывод дешифрованого текста с каждым отступом

    else: # если отступ известен
        print("\nOutput text: {}".format(encrypt(language, int(indent), text))) # вывод шифрованного/дешифрованого текста

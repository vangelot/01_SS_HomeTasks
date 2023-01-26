'''
ps_04_03 = 4th Homework, task #3, ps = Свалявчик П.

Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає
відповідно True чи False. Паліндром - це слово, яке однаково читається
зліва направо та справа наліво. Наприклад, "випив"
'''

def is_polindrom(word):
    print(len(word))
    if len(word) <= 1:
        return True
    elif len(word) == 2:
        print(word)
        if word[0] == word[1]:
            print('dadada')
            return True
        else:
            return False
    else:
        print('hi', word)
        while len(word) >= 3:
            if word[0] == word[-1]:
                word = word[1:] # видаляєм перший символ
                word = word[:-1] # видаляєм останній символ
                is_polindrom(word)
            else:
                return False

print(is_polindrom('aaddaa'))
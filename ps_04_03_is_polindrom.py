'''
ps_04_03 = 4th Homework, task #3, ps = Свалявчик П.

Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає
відповідно True чи False. Паліндром - це слово, яке однаково читається
зліва направо та справа наліво. Наприклад, "випив"
'''

def is_polindrom(word):
    while len(word) >= 3:
        if word[0] == word[-1]:
            word = word[1:] # видаляєм перший символ
            word = word[:-1] # видаляєм останній символ
        else:
            return False
    if word[0] == word[-1]:
        return True
    else:
        return False

print(is_polindrom('aabbaaa')) # для перевірки
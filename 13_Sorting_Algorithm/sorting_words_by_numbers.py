import random
from sorting_words import quick_sort_words
# реалізація через переведення слова в Флоат, але не вистачає розрядів для латиниці
def word_to_number(word):
    num = 0.0
    alfa = 0 # minus 1000 if cyrillic
    beta = 10 # для латиниці 3 розряди, для кирилиці 2
    if ord(word[0]) > 1000:
        alfa = 1000
        beta = 1
    for i in range(len(word)):
        num = num + (ord(word[i])-alfa)*((beta*100)**(-i))
    return num

def word1_bigger_word2(word1, word2):
    if word_to_number(word1) > word_to_number(word2):
        return True
    elif word_to_number(word1) < word_to_number(word2):
        return False
    else:
        return None


list = ['Каша', "Рыба", "мясо", "олень", "Алёшка", "алежка", "молочко", "Париж", "Курица",
        "гомогей", "пионер", "путинЛох", "Стабилизаторчик", "Стабилизатор", "стоянка"]

print(list)
print(quick_sort_words(list))

# довгі слова Стабилизатор - Стабилизаточрик - для нього вжее однакові, але на коротких все працює
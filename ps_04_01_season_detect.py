'''
ps_04_01 = 4th Homework, task #1, ps = Свалявчик П.

Напишіть функцію, яка приймає номер місяця та повертає рядок з назвою пори року, до якої
цей місяць відноситься
'''

seasons = {
    # Словник пір року
    1 : "Winter",
    2 : "Winter",
    3 : "Spring",
    4 : "Spring",
    5 : "Spring",
    6 : "Summer",
    7 : "Summer",
    8 : "Summer",
    9 : "Autumn",
    10: "Autumn",
    11: "Autumn",
    12: "Winter"
}

def season_detect(month_number):
    '''
    Отримує номер місяця: якщо на вході числа 1-12 повертає назву місяця,
    Якщо ввели ***ню повертає теж саме)
    '''
    try:
        month_number = int(month_number)
    except:
        return "Некоректний ввод"

    if month_number in seasons.keys():
        for key, value in seasons.items():
            if key == month_number:
                return value
    else:
        return "No such month"
print(season_detect(input("Введіть номер місяця: ")))

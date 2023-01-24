
# file = open (r'D:\_DATA SCIENCE\CourseProjects\111.txt', encoding='utf-8')
# file = open ('111.txt', 'a+', encoding='utf-8')
# file.seek(0)
# print(file.read(5))
#
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
    10.1: "Autumn",
    11: "Autumn",
    'a': "Winter",
    22 : 55,
    (1,2) : 555,
    '22' : "100"
}

def file_filling (name, dic={}):
    try:
        file = open(name, 'w')
        # file.write('hello')
        # ми будемо перевіряти, чи є тип ключа стрінгом, а також чи є тип значення
        # словника стрінгом
        for key, value in dic.items():
            if type(key) == str and type(value) != str:
                file.write('"'+str(key)+'":'+str(dic[key])+'\n')
            elif type(key) == str and type(value) == str:
                file.write('"'+str(key) + '":"' + str(dic[key]) + '"\n')
            elif type(value) == str:
                file.write(str(key) + ':"' + str(dic[key]) + '"\n')
            else:
                file.write(str(key) + ':' + str(dic[key]) + '\n')
        file.close()
    except:
        print("Smth went wrong, try again later")
        pass

file_filling('224.txt', seasons)


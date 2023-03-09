'''
ps_04_02 = 4th Homework, task #2, ps = Свалявчик П.

Напишіть функцію, яка приймає довільну кількість словників, збирає їх
в один словник та повертає його
'''

def combine_dics(*dics):
    result_dic = {}
    for i in dics:
        result_dic.update(i)
    return result_dic

# для прикладу (про повтори ключів нічого не сказано)
print(combine_dics({1: '22', 'a': "44"},{'b': 10, 1: '223'}))

'''
ps_04_05 = 4th Homework, task #5, ps = Свалявчик П.

Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається в
ньому найчастіше
'''


def max_letter(str):
    max_count = 1
    max_index = 0
    list_of_sum = []
    list_of_letters = list(str)
    for i in range(len(list_of_letters)):
        list_of_sum.append(1)
        for j in range(i+1, len(list_of_letters)):
            if list_of_letters[j] == list_of_letters[i]:
                list_of_sum[i] += 1
                # print(max_count)
                if list_of_sum[i] > max_count:
                    max_count = list_of_sum[i]
                    max_index = i
    return list_of_letters[max_index]

print(max_letter('abcaaccccaaaaccc'))

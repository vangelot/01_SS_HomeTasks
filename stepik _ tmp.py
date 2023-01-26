# def list_sum(lst):
#     result = ''
#     for element in lst:
#         result += element
#     return result
#
# def sum(a, b):
#     return a + b
#
# y = sum(14, 29)
# z = list_sum(['1', 'd', 'a'])
# print(y)
# print(z)

def printab(a,b):
    print(a)
    print(b)
# printab(10,20)
lst=[10,20]
printab(*lst)

args = {'b' : 12, 'a' : 20}
printab(**args)
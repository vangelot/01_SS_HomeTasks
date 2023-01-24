#
# a = 'a'
# print(str(a))
#
# dict = {}
#
# dict.update({1: 2})
# print(dict)
#
# a = 'asdf'
# if 's' in a:
#     print(a)

a = 12434
res = 0
print(str(a))

for i in range(len(str(a))):
    ost = a % 10
    res += ost*(10 ** (len(str(a))-1))
    a = a // 10

print(res)
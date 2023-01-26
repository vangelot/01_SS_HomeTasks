list_of_str = ['abc', 'aaaeer', 'bca', 'aaa', 'bbddda']
vowels = ['a', 'o', 'e', 'u', 'i', 'y']

def list_res(list):
    return [x for x in list if (len(x) <= 5) * (x[0] in vowels)]

print(list_res(list_of_str))

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
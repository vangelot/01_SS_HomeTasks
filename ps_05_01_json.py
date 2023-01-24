import json
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
    11.1: "Autumn",
    'a': "Winter",
    22 : 55,
    #(1 ,2) : 555,
    '22' : 100
}

def file_filling (name, dict={}):
    with open (name, 'w') as file:
        # for key in dict:
        json.dump(dict, file, indent=4)

file_filling('224.json', seasons)

    # file = open(name, 'w')
    # # file.write('hello')
    # for key in dic:
    #     file.write(str(key)+': '+str(dic[key])+'\n')
    # file.close()

# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# '["foo", {"bar": ["baz", null, 1.0, 2]}]'
#
# print(json.dumps({'4': 5, '3': 7, '8': 1}, sort_keys=True, indent=4))


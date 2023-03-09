def line_to_keyvalue(line):
    key = ''
    value = ''
    index = 0
    # tuple = (key, value)
    while line[index] != ':':
        # print(index)
        key += line[index]
        index += 1
    index += 1
    try:
        while line[index] != '\n':
            value += line[index]
            index += 1
    except:
        pass
    if key[0] == '(':
        key = key[1:-1]
        key = tuple(map(int, key.split(',')))
    elif key[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and '.' in key:
        key = float(key)
    elif key[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and '.' not in key:
        key = int(key)

    if value[0] == '(':
        value = value[1:-1]
        value = tuple(map(int, value.split(', ')))
    elif value[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and '.' in value:
        value = float(value)
    elif value[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') and '.' not in value:
        value = int(value)
    return key, value
def dict_create(file_name):
    file = open(file_name, 'r')
    list_of_lines = file.readlines()
    dict_result = {}

    for line in list_of_lines:
        dict_result.update({line_to_keyvalue(line)})
    file.close()
    return dict_result

print(dict_create('224.txt'))

#print(line_to_keyvalue('"1":'))
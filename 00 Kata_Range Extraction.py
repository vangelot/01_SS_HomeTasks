def solution(args):
    # your code here
    res = ''
    i = 0
    while i <= len(args) - 3: #генеральный цикл доходим до конца
            if (args[i]+1 == args[i+1]) and (args[i+1]+1 == args[i+2]):
                res += str(args[i]) + '-'
                while (args[i] + 1 == args[i+1]):
                    i += 1
                    if i == len(args)-1:
                        break
                if i == len(args)-1:
                    res += str(args[i])
                    return res
                else:
                    res += str(args[i]) + ','
                i += 1
            else:
                res += str(args[i]) + ','
                i += 1
    if i == len(args)-2:
        res += str(args[i]) + ','
        i += 1
    if i == len(args)-1:
        res += str(args[i])
        i += 1
            #print('yes')
    return res
#print(solution([1, 2]))
print(solution([1, 3, 4, 5, 7, 8, 9]))
# '-6,-3-1,3-5,7-11,14-15,17-20' should equal
# '-6,-3-1,3-5,7-11,14,15,17-20'
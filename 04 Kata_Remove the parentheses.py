def remove_parentheses(s):
    i = 0
    res=''
    while i < len(s):
        if (s[i] == "(") and (")" in s[0:i]+s[i+1:]):
            remove_parentheses(res + s[0:i]+s[i+1:])
            #i += 1
            while s[i] != ")":
                i += 1
            i += 1
            res += s[i]
            i += 1
        else:
            res += s[i]
            i += 1
    return res
print(remove_parentheses('(((f)x'))
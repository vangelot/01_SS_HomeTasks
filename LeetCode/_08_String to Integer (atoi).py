class Solution:
    digits = '0123456789'
    def myAtoi(self, s: str) -> int:
        i = 0
        j = 1
        res = ''
        flag = False
        if s == '':
            return 0
        res_num = 0
        while i < len(s) and s[i] not in self.digits:
            if s[i] == ' ':
                i += 1
            elif s[i] == '-':
                j *= -1
                if i+1 < len(s) and s[i+1] not in self.digits:
                    return 0
                if flag:
                    return 0
                flag = True
                i += 1
            elif s[i] == '+':
                if flag:
                    return 0
                if i+1 < len(s) and s[i+1] not in self.digits:
                    return 0
                flag = True
                i += 1
            else:
                return 0
        while i < len(s) and s[i] in self.digits:
            print(i)
            res += s[i]
            print('res=', res)
            i += 1
        if res == '':
            return 0
        if int(res)*j > 2147483647:
            return 2147483647
        if int(res)*j < -2147483648:
            return -2147483648

        return int(res)*j


def main():
    print('hello')
    a = Solution()
    print(a.myAtoi('   --123222222222222 a'))
    print(a.myAtoi('+'))
    pass


if __name__ == '__main__':
    main()

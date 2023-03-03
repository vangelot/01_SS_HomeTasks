class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1
        print(len(needle), len(haystack))
        for i in range(len(haystack)-len(needle)+1):
            print('i=', i)
            for j in range(len(needle)):
                flag = 0
                print('j=', j)
                if needle[j] != haystack[i+j]:
                    print('break')
                    flag = 1
                    break
            if flag == 0:
                return i
        return -1


def main():
    print('hello')
    a = Solution()
    print(a.strStr('bbqabc', 'qabc'))
    pass


if __name__ == '__main__':
    main()
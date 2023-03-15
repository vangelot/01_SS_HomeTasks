class Solution:
    def isValid(self, s: str) -> bool:

        while ('()' in s) or ('[]' in s) or ('{}' in s):
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('()', '')
        if len(s) == 0:
            return True
        else:
            print(s)
            return False


def main():
    print('hello')
    a = Solution()
    b = '{{}()}'
    print(a.isValid(b))

    pass


if __name__ == '__main__':
    main()
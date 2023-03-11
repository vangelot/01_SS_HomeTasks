class Solution:

    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        length = len(x_str)
        if x_str[0] == '-' or (length > 1 and x_str[0] != x_str[-1]):
            return False
        elif length == 0 or length == 1:
            return True
        elif length == 2 and x_str[0] == x_str[1]:
            return True
        else:

            return self.isPalindrome(x_str[1:-1])


def main():
    print('hello')
    a = Solution()
    # b = 'abc'
    # print(b[-1])
    print(a.isPalindrome(101))
    pass


if __name__ == '__main__':
    main()
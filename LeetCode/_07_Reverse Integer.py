class Solution:
    def reverse(self, x: int) -> int:
        is_positive = 1
        x_str = str(x)
        res_int = 0
        if x_str[0] == '-':
            is_positive = -1
            x_str = x_str[1:]

        for pointer in range(len(x_str)):
            res_int += int(x_str[pointer]) * 10**pointer

        res_int *= is_positive
        if -2**31 <= res_int <= 2**31 - 1:
            return res_int
        else:
            return 0


def main():
    print('hello')

    a = Solution()
    print(a.reverse(-125))
    pass


if __name__ == '__main__':
    main()

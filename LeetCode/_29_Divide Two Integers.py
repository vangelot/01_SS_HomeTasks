class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        is_positive = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            is_positive = -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = - divisor

        if divisor == 0:
            return None

        res = 0
        if divisor == 1:
            if is_positive == 1:
                if dividend > 2147483647:
                    return 2147483647
                else:
                    return dividend
            else:
                return -dividend

        while dividend >= divisor:
            exp = 1
            while divisor ** (exp + 1) < dividend:
                exp += 1

            dividend -= divisor ** exp
            res += divisor ** (exp - 1)

        if is_positive == 1:
            return res
        else:
            return -res


def main():
    print('hello')
    a = Solution()

    print(a.divide(10000, 2))


if __name__ == '__main__':
    main()
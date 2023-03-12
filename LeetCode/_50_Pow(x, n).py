class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0
        if x == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        elif n > 1:
            res = x * x
            _pow = 2
            delta = 0.000000000000000000000000000001
            flag = False
            while _pow * 2 <= n:
                if (res - res * res < delta) and res < 1:
                    flag = True
                    break
                res = res * res
                _pow = _pow * 2
            if not flag:
                for i in range(_pow, n):
                    res = res * x
            return res

        else:
            res = 1 / (x * x)
            _pow = 2
            delta = 0.000000000000000000000000000001
            flag = False
            while _pow * 2 <= -n:
                if abs(res - res * res) < delta:
                    flag = True
                    break
                res = res * res
                _pow = _pow * 2
            if not flag:
                for i in range(_pow, -n):
                    res = res / x
            return res

def main():
    print('hello')
    a = Solution()

    print(a.myPow(8.84372, -5))


if __name__ == '__main__':
    main()
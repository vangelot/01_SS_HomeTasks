class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        _dict = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }
        res = []

        if len(digits) == 0:
            return []

        for first in _dict[digits[0]]:
            if len(digits) > 1:
                for second in _dict[digits[1]]:
                    if len(digits) > 2:
                        for third in _dict[digits[2]]:
                            if len(digits) > 3:
                                for fourth in _dict[digits[3]]:
                                    res.append(first+second+third+fourth)
                            else:
                                res.append(first+second+third)
                    else:
                        res.append(first+second)
            else:
                res.append(first)
        return res


def main():
    print('hello')
    a = Solution()

    print(a.letterCombinations('223'))


if __name__ == '__main__':
    main()

class Solution:

    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            if s[i] == 'M':
                sum += 1000
                i += 1
            elif s[i] == 'C':
                if i < len(s) - 1:
                    if s[i+1] == 'M':
                        sum += 900
                        i += 2
                        continue
                    elif s[i+1] == 'D':
                        sum += 400
                        i += 2
                        continue
                sum += 100
                i += 1
            elif s[i] == 'D':
                sum += 500
                i += 1
            elif s[i] == 'X':
                if i < len(s) - 1:
                    if s[i+1] == "C":
                        sum += 90
                        i += 2
                        continue
                    elif s[i+1] == 'L':
                        sum += 40
                        i += 2
                        continue
                sum += 10
                i += 1
            elif s[i] == 'L':
                sum += 50
                i += 1
            elif s[i] == 'I':
                if i < len(s) - 1:
                    if s[i+1] == 'X':
                        sum += 9
                        i += 2
                        continue
                    elif s[i+1] == 'V':
                        sum += 4
                        i += 2
                        continue
                sum += 1
                i += 1
            elif s[i] == 'V':
                sum += 5
                i += 1
        return sum


def main():
    a = Solution()
    print(a.romanToInt('MCDLXIX'))
    print(a.romanToInt('LVIII'))
    pass


if __name__ == '__main__':
    main()

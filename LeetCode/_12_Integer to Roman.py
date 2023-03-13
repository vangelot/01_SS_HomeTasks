class Solution:
    def intToRoman(self, num: int) -> str:

        _dict = {
            1: 'I',     10: 'X',    100: 'C',   1000: 'M',
            2: 'II',    20: 'XX',   200: 'CC',  2000: 'MM',
            3: 'III',   30: 'XXX',  300: 'CCC', 3000: 'MMM',
            4: 'VI',    40: 'LX',   400: 'DC',
            5: 'V',     50: 'L',    500: 'D',
            6: 'IV',    60: 'XL',   600: 'CD',
            7: 'IIV',   70: 'XXL',  700: 'CCD',
            8: 'IIIV',  80: 'XXXL', 800: 'CCCD',
            9: 'XI',     90: 'CX',  900: 'MC'
        }
        num_string = str(num)[::-1]

        res = ''
        for _pow in range(len(num_string)):
            if num_string[_pow] == '0':
                continue
            res += _dict[10**_pow*int(num_string[_pow])]
        return res[::-1]


def main():
    print('hello')
    a = Solution()

    print(a.intToRoman(10))

    # HOW TO REVERSE STRING:
    # b = '123'
    # b = b[::-1]
    # print(b) # '321'

if __name__ == '__main__':
    main()
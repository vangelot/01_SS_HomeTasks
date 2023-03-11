
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res_str = ''
        if numRows == 1:
            return s
        if numRows == 2:
            pointer = 0
            while pointer < len(s):
                res_str += s[pointer]
                pointer += 2
            pointer = 1
            while pointer < len(s):
                res_str += s[pointer]
                pointer += 2
            return  res_str

        for pointer in range(0, len(s), numRows*2 - 2):
            print(pointer)
            res_str += s[pointer]

        for row in range(1, numRows - 1):
            pointer = row
            while pointer < len(s):
                res_str += s[pointer]
                pointer += (numRows - row - 1) * 2
                if pointer < len(s):
                    res_str += s[pointer]
                else:
                    break
                pointer += row * 2

        for pointer in range(numRows - 1, len(s), numRows * 2 - 2):
            res_str += s[pointer]

        return res_str


def main():
    print('hello')

    a = Solution()
    print(a.convert('abcdeab', 4))
    pass


if __name__ == '__main__':
    main()

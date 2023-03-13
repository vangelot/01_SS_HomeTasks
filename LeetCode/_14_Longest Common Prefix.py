class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs:
            min_len = len(strs[0])
        else:
            return ''

        for words in strs:
            if len(words) < min_len:
                min_len = len(words)
                if min_len == 0:
                    return ''
        res = ''

        for index in range(min_len):
            for words_index in range(1, len(strs)):
                if strs[words_index][index] != strs[0][index]:
                    return res
            res += strs[0][index]

        return res


def main():
    print('hello')
    a = Solution()

    print(a.longestCommonPrefix(['ab', 'abc', 'abbbbb']))
    # print(a.longestCommonPrefix([]))
    b = ''
    print(len(b))

if __name__ == '__main__':
    main()

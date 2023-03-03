class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_word = ''
        i = 0
        cur_word = ''
        if len(s) == 1:
            return 1
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                cur_word = s[i] + s[i+1]
                if len(cur_word) > len(max_word):
                    max_word = cur_word[:]
                i += 1
                j = i
                while j < len(s)-1 and s[j+1] not in cur_word:
                    cur_word += s[j+1]
                    j += 1
                    if len(cur_word) > len(max_word):
                        max_word = cur_word[:]
                        # print(max_word)
                        # print(max_word)
            else:
                cur_word = s[i+1]
                if len(cur_word) > len(max_word):
                    max_word = cur_word[:]
                i += 1
        return len(max_word)


def main():
    print('hello')
    a = Solution()
    print(a.lengthOfLongestSubstring('asdfaq'))
    pass


if __name__=='__main__':
    main()
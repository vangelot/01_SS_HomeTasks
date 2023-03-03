class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_poli = ''
        for i in range((len(s)-1)*2):
            print(i)
            poli = self.build_polindrome(s, i)
            if len(poli) > len(max_poli):
                max_poli = poli
        return max_poli

    def build_polindrome(self, s: str, i: int):
        shift = 2
        res = ''
        if i % 2 == 0:
            res = s[i // 2]
            while i - shift >= 0 and i + shift <= (len(s)-1)*2:
                if s[(i+shift) // 2] == s[(i-shift) // 2]:
                    res = s[(i-shift) // 2] + res + s[(i+shift) // 2]
                    shift += 2
                else:
                    return res
        elif i % 2 == 1:
            while i - shift + 1 >= 0 and i + shift -1 <= (len(s)-1)*2:
                if s[(i+shift-1) // 2] == s[(i-shift+1) // 2]:
                    res = s[(i-shift+1) // 2] + res + s[(i+shift-1) // 2]
                    shift += 2
                else:
                    return res
                pass
        return res
def main():
    print('hello')
    a = Solution()
    print(a.longestPalindrome('bb'))
    # print(a.build_polindrome('bb',1))

    pass


if __name__=='__main__':
    main()
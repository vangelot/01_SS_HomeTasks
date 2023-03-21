class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] == 0:
                sub_length = 0
                while i < len(nums) and nums[i] == 0:
                    sub_length += 1
                    i += 1
                res += sub_length*(sub_length-1)/2 + sub_length
            else:
                i += 1
        return int(res)


def main():
    a = Solution()
    print(a.zeroFilledSubarray([1,0,0,0,0,1]))


if __name__ == '__main__':
    main()
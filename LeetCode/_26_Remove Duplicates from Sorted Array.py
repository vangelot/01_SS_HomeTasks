class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        while p < len(nums)-1:
            while (p < len(nums)-1) and (nums[p] == nums[p+1]):
                nums.remove(nums[p])
            p += 1
        return len(nums)


def main():
    print('hello')
    a = Solution()
    b = [10, 10, 10, 20, 20, 30, 30]
    print(a.removeDuplicates(b))
    print(b)
    # b.remove(1)

    # HOW TO REVERSE STRING:
    # b = '123'
    # b = b[::-1]
    # print(b) # '321'


if __name__ == '__main__':
    main()
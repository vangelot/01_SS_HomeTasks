import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) > 1:
            pivot = random.choice(nums)
            less = [x for x in nums if x < pivot]
            greater = [x for x in nums if x > pivot]
            equal = [x for x in nums if x == pivot]
            return self.sortArray(less) + equal + self.sortArray(greater)
        else:
            return nums


def main():
    print('hello')
    a = Solution()

    print(a.sortArray([1, 3, 1, 4, 5, 1]))


if __name__ == '__main__':
    main()
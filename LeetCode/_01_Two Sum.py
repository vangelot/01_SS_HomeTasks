class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in seen:
                return [seen[second], i]
            else:
                seen[nums[i]] = i


def main():
    print('hello')
    a = Solution()
    print(a.twoSum([2,5,5,11], 10))
    # print(a.twoSum([-1, -2, -3, -4, -5], -8))
    # print(a.twoSum([1,6142,8192,10239], 18431))
    # print(a.int_to_index([2, 5, 5, 11], 5, 5))

    pass


if __name__ == '__main__':
    main()
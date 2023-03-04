class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

            if len(nums) == 2:
                return [0, 1]
            if len(nums) == 3:
                if nums[0]+nums[1] == target:
                    return [0, 1]
                elif nums[0]+nums[2] == target:
                    return [0, 2]
                else:
                    return [1, 2]
            # backup = nums[:]
            # nums.sort()
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
            pass


def main():
    print('hello')
    a = Solution()
    print(a.twoSum([1,3,4,2], 6))
    # print(a.twoSum([-1, -2, -3, -4, -5], -8))
    # print(a.twoSum([1,6142,8192,10239], 18431))
    # print(a.int_to_index([2, 5, 5, 11], 5, 5))

    pass


if __name__ == '__main__':
    main()
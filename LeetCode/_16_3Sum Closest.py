class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        min_delta = target - res

        for first in range(len(nums)-2):
            left = first+1
            right = len(nums)-1
            while left < right:
                sum3 = nums[first] + nums[left] + nums[right]
                if abs(sum3 - target) < min_delta:
                    min_delta = abs(sum3 - target)
                    res = sum3
                if sum3 == target:
                    return target
                elif sum3 < target:
                    left += 1
                elif sum3 > target:
                    right -= 1

        return res


def main():
    print('hello')
    a = Solution()

    print(a.threeSumClosest([1, 2, -1, 4], 1))


if __name__ == '__main__':
    main()

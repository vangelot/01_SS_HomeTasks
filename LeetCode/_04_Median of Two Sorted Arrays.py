class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_list = nums1 + nums2
        res_list.sort()
        while len(res_list) > 2:
            res_list = res_list[1:-1]
        if len(res_list) == 1:
            return res_list[0]
        else:
            return (res_list[0]+res_list[1]) / 2
        pass


def main():
    print('hello')
    a = Solution()
    print(a.findMedianSortedArrays([1,2],[3,4,1]))
    b = [1, 2, 3]
    b = b[1:-1]
    print(b)
    pass


if __name__ == '__main__':
    main()
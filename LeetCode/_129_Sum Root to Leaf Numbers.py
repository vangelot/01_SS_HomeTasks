# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # res = 0

    def sumNumbers(self, root: [TreeNode]) -> int:
        self.res = 0
        cur_num = 0
        self.get_sum(root, cur_num)
        return self.res

    def get_sum(self, root, cur_num):
        if root:
            if not root.right and not root.left:
                self.res += cur_num*10 + root.val
            self.get_sum(root.left, root.val + 10*cur_num)
            self.get_sum(root.right, root.val + 10*cur_num)



def main():
    print('hello')
    a = Solution()

    node1 = TreeNode(4)
    node1.left = TreeNode(9, TreeNode(5), TreeNode(1))
    node1.right = TreeNode(0)

    node2 = TreeNode(1, TreeNode(0))

    node3 = TreeNode(8, TreeNode(3, right=TreeNode(9, TreeNode(9), TreeNode(5))), TreeNode(5))

    print(a.sumNumbers(node1))
    # print(a.sumNumbers(node3))


if __name__ == '__main__':
    main()
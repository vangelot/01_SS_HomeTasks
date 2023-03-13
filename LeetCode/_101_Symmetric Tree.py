
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.is_2_symmetric(root.left, root.right)
        pass

    def is_2_symmetric(self, node1, node2):
        if (node1 and not node2) or (node2 and not node1):
            return False
        elif not node1 and not node2:
            return True
        elif node1.val != node2.val:
            return False
        else:
            return bool(self.is_2_symmetric(node1.left, node2.right)*self.is_2_symmetric(node1.right, node2.left))


def main():
    print('hello')
    a = Solution()

    node1 = TreeNode(10)
    node1.left = TreeNode(5, TreeNode(10))
    node1.right = TreeNode(5, right=TreeNode(11))

    print(a.isSymmetric(node1))


if __name__ == '__main__':
    main()
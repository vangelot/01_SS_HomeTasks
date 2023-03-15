class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: [TreeNode]) -> bool:
        return self.is_complete2(root.left, root.right)

    def depth_detect(self, node):
        lev = 0
        while node.left:
            lev += 1
            node = node.left
        return lev

    def is_complete(self, node, lev):
        if lev == 0:
            return True
        if lev == 1 and node.left and node.right:
            return True
        elif lev > 0 and not node.left or not node.right:
            return False
        else:
            lev -= 1
            return bool(self.is_complete(node.left, lev) * self.is_complete(node.right, lev))

    def is_complete2(self, node1, node2):
        if not node1 and not node2:
            return True
        if node2 and not node1:
            return False
        if node1 and not node2:
            if node1.left or node1.right:
                return False
            else:
                return True
        if node1 and node2:
            left_depth = 0
            right_depth = 0
            n1, n2 = node1, node2
            while n1.left:
                left_depth += 1
                n1 = n1.left
            while n2.right:
                right_depth += 1
                n2 = n2.right
            if abs(left_depth - right_depth) > 1:
                return False

            if self.depth_detect(node1) == self.depth_detect(node2):
                if not self.is_complete(node1, self.depth_detect(node1)):
                    print(node1.val, node2.val, self.depth_detect(node1))
                    return False
            if (not node1.left or not node1.right) and (node2.left or node2.right):
                return False
            if node1.left and (node1.left.left or node1.left.right) and (not node2.left or not node2.right):
                return False
            if node1.left and node1.right and node2.left:
                if (not node1.right.left or not node1.right.right) and (node2.left.left or node2.left.right) and (
                        node1.left.left or node1.left.right):
                    return False
            return bool(self.is_complete2(node1.left, node1.right) * self.is_complete2(node2.left, node2.right))


def main():
    print('hello')
    a = Solution()

    node1 = TreeNode(1)
    node1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    node1.right = TreeNode(3, TreeNode(6))

    node2 = TreeNode(1, TreeNode(0))

    node3 = TreeNode(8, TreeNode(3, right=TreeNode(9, TreeNode(9), TreeNode(5))), TreeNode(5))

    # print(a.is_complete(node1.left, 1))
    # print(a.depth_detect(node1))
    print(a.isCompleteTree(node1))
    # print(a.sumNumbers(node3))


if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: list[int], postorder: list[int]) -> [TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        ind = 0
        left_i = []
        right_i = []
        while inorder[ind] != postorder[-1]:
            left_i.append(inorder[ind])
            ind += 1
        ind += 1
        while ind < len(inorder):
            right_i.append(inorder[ind])
            ind += 1
        left_p = []
        right_p = []
        for ind in range(len(left_i)):
            left_p.append(postorder[ind])
        for ind in range(len(right_i)):
            right_p.append(postorder[ind+len(left_i)])

        root.left = self.buildTree(left_i, left_p)
        root.right = self.buildTree(right_i, right_p)
        # print(left_i, right_i)
        # print(left_p, right_p)
        # print(root.val)
        # while root:
        #     print(root.val)
        #     root = root.left
        # print(root.val, root.left.val, root.right.val)
        return root



def main():
    print('hello')
    a = Solution()

    a.buildTree([8, 9, 10, 3, 7, 20, 4], [8, 10, 9, 7, 4, 20, 3])



if __name__ == '__main__':
    main()

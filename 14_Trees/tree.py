from Trees import Tree


# preorder traversal
def pre_oder(node):
    if node:
        print(node.id_node)
        pre_oder(node.left)
        pre_oder(node.right)


# postorder traversal
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.id_node)


# inorder traversal
def in_order(node):
    if node:
        in_order(node.left)
        print(node.id_node)
        in_order(node.right)


tree = Tree(1)
tree.left = Tree(2)
tree.left.left = Tree(3)
tree.left.right = Tree(4)
tree.right = Tree(5)

tree.insert(7)
tree.insert(12)
tree.insert(8)
tree.insert(22)
tree.insert(14)

print(tree)


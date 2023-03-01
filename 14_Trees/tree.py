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


tree = Tree(10)


tree.insert(6)
tree.insert(4)
tree.insert(8)
tree.insert(22)
tree.insert(14)

print(tree.left)
print(tree.right)
print(tree.left.left)
print(tree.left.right)
# tree.print_tree()

# print(tree.right.right.right.left)
# print(tree.right.right.right.right)
# print(tree.right.right.right.right.left)
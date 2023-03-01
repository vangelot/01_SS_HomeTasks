from Trees import Tree


def main():
    tree = Tree(12)

    tree.add_list_nodes([10, 9, 11, 'QQQ', 22, 14, 2, 24.5, 'a', 10])

    print(tree.left)
    print(tree.right)
    print(tree.left.left)
    print(tree.left.right)
    print(tree.left.left.right)

    print("min element is: ", tree.find_min())
    print("max element is: ", tree.find_max())


if __name__ == '__main__':
    main()

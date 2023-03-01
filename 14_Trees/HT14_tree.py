from Trees import Tree


def main():
    tree1 = Tree(12)
    print("\nADDING NODES TO    three1:\n")
    tree1.add_list_nodes([10, 9, 11, 'QQQ', 22, 14, 2, 24.5, 'a', 10])
    print("")

    print("min element is: ", tree1.find_min())
    print("max element is: ", tree1.find_max())

    tree2 = Tree(-3)
    print("\nADDING NODES TO    three2:\n")
    tree2.add_list_nodes([-5, -6, -4, 4, 6, 5, 8, 7, -1, -2, 3, 1, 0, 2])
    print("")

    # видалення: працює на всіх прикладах крім видалення root node.
    # в файлі є візуалізація дерева яке вийшло, щоб можна було щось видалити і подивитись
    # на результат через print(tree2.right.left....etc)

    # саме цікаве видалення:
    tree2.delete_node(4)

    print(tree2.right.left.right)
    # print(None.find_node(10))


if __name__ == '__main__':
    main()

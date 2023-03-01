def levels_detect(num_of_values):
    levels = 0
    rest = num_of_values - 2
    levels = 1
    while rest > 0:
        levels += 1
        rest = rest - 2**levels
    return levels


class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None
        # self.adding_counter = 0
        # self.graph=[]

    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if id_node <= self.id_node:
            if self.left is None:
                self.left = Tree(id_node)
            else:
                self.left.insert(id_node)
        elif id_node > self.id_node:
            if self.right is None:
                self.right = Tree(id_node)
            else:
                self.right.insert(id_node)

        # ЦЕ НЕПРАВИЛЬНИЙ КОД, ЯКИЙ ВЕДЕ ДО ПЕРЕЗАТИРАННЯ НУЛЯ В ДЕРЕВІ
        # і взагалі він тут не потрібен
        # else:
        #     self.id_node = id_node

    # find_val method to compare the id_node with nodes
    def find_val(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    def add_list_nodes(self, _list):
        for node in _list:
            # self.insert(node)
            try:
                self.insert(node)
                print(f"node {node} added to tree")
            except:
                print(f"node {node} can't be added to tree")
        pass

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self

    def find_node(self, node_value):
        if node_value == self.id_node:
            return self
        elif node_value < self.id_node:
            if self.left:
                return self.left.find_node(node_value)
            else:
                print("no such node")
                return None
        elif node_value > self.id_node:
            if self.right:
                return self.right.find_node(node_value)
            else:
                print("no such node")
                return None

    def find_parent(self, node):
        if self == node:
            return self, 0
        elif node.id_node > self.id_node:
            if self.right == node:
                return self, 1
            else:
                return self.right.find_parent(node)
        elif node.id_node <= self.id_node:
            if self.left == node:
                return self, -1
            else:
                return self.left.find_parent(node)
        pass

    def delete_node(self, node_value):
        print("! we are in DELETE method !")

        node_to_del = self.find_node(node_value)

        if node_to_del.left:
            node_to_insert = node_to_del.left.find_max()
        else:
            node_to_insert = node_to_del
            pass

        node_to_del_parent = self.find_parent(node_to_del)
        node_to_insert_parent = node_to_del.find_parent(node_to_insert)

        print("node to delete: ", node_to_del)
        print("node to insert:", node_to_insert)
        print("node to del Parent: ", node_to_del_parent[0])
        print("node to insert Parent: ", node_to_insert_parent[0])

        if node_to_del.left and node_to_del.right:
            if node_to_del_parent[1] == 1:
                node_to_del_parent[0].right = node_to_insert
                if node_to_insert_parent[0] != node_to_del:
                    node_to_insert_parent[0].right = node_to_insert.left
                    node_to_insert.left = node_to_insert_parent[0]
                node_to_insert.right = node_to_del.right
            if node_to_del_parent[1] == -1:
                node_to_del_parent[0].left = node_to_insert
                if node_to_insert_parent[0] != node_to_del:
                    node_to_insert_parent[0].right = None
                    node_to_insert.left = node_to_insert_parent[0]
                node_to_insert.right = node_to_del.right

        elif node_to_del.left is None and node_to_del.right is None:
            if node_to_del_parent[1] == 1:
                node_to_del_parent[0].right = None
            elif node_to_del_parent[1] == -1:
                node_to_del_parent[0].left = None
        elif node_to_del.right is None:
            node_to_del_parent[0].right = node_to_insert
        elif node_to_del.left is None:
            node_to_del_parent[0].left = node_to_del.right



        pass
    # def add_bts_node(self, value):
    #     if value is None:
    #         self.adding_counter = 1
    #         self.graph.append(value)
    #         return True
    #
    #     if self.adding_counter % 2 == 0:
    #         if value <= self.id_node:
    #             self.left = Tree(value)
    #             self.graph.append(value)
    #             self.adding_counter += 1
    #             return True
    #         else:
    #             return False
    #     elif self.adding_counter % 2 == 1:
    #         if value >= self.id_node:
    #             self.right = Tree(value)
    #             self.graph.append(value)
    #             self.adding_counter += 1
    #             return True
    #         else:
    #             return False

    # def add_bts_graph(self, _list):
    #     levels = levels_detect(len(_list))
    #     for i in range(1, levels+1):
    #         for j in range(1, 2**i+1):
    #             pass
    #     pass

    # def add_bts_level(self, list_nodes, list_values):
    #     value_index = 0
    #     for node in list_nodes:
    #         if node.add_bts_node(list_values[value_index]):
    #             node.add_bts_node(list_values[value_index])
    #         else:
    #             return False
    #         value_index += 1
    #         if node.add_bts_node(list_values[value_index]):
    #             node.add_bts_node(list_values[value_index])
    #         else:
    #             return False
    #         value_index += 1
    #     return True


if __name__ == "__main__":
    pass
    # a = Tree(10)
    # b = Tree(11)
    #
    # print(a)
    # # print(a.add_bts_level([a], [9, 12]))
    # print(a.graph)
    # print(a.left)
    # print(a.right)
    #
    # print(levels_detect(14))

    # trying to add in left:
    # b.add_bts_node(5)
    #
    # # trying to add in right: nothing happens:
    # print(b.add_bts_node(5))
    # print("b.left=", b.left)
    # print("b.right=", b.add_bts_node(12), ',', b.right)
    #
    # a.add_bts_node(None)
    # if a.add_bts_node(11):
    #     a.add_bts_node(11)
    # print(a.left)
    # print(a.right)
    #
    # print(a._tmp([1, 2, 6, 7, 10, 11]))





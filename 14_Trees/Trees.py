class Tree:
    BTS_adding_counter = 0

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    #Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

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

    def add_bts_node(self, value):
        if value is None:
            self.__class__.BTS_adding_counter += 1
            return True
        # elif value < self.id_node:
        #     if self.left is None:
        #         self.left = Tree(value)
        #         return 1
        #     else:
        #         return -1
        # elif value > self.id_node:
        #     if self.right is None:
        #         self.right = Tree(value)
        #         return 1
        #     else:
        #         return -1
        # elif value == self.id_node:
        #     if
        if self.__class__.BTS_adding_counter % 2 == 0:
            if value <= self.id_node:
                self.left = Tree(value)
                self.__class__.BTS_adding_counter += 1
                return True
            else:
                return False
        elif self.__class__.BTS_adding_counter % 2 == 1:
            if value >= self.id_node:
                self.right = Tree(value)
                self.__class__.BTS_adding_counter += 1
                return True
            else:
                return False


a = Tree(10)
b = Tree(11)
print("B=", b)
b.add_bts_node(5)
print("b.left=", b.left)
a.add_bts_node(None)
if a.add_bts_node(11):
    a.add_bts_node(11)
print(a.left)
print(a.right)
# a.left.insert(5)
# print(a.left)
# print(a)




class Node:
    def __init__(self, val=None):
        # self.val = val
        self.children = {}
        self.is_passed = False

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        dict_of_nodes = {}
        for road in roads:
            if road[0] not in dict_of_nodes.keys():
                dict_of_nodes[road[0]] = Node()
            if road[1] not in dict_of_nodes.keys():
                dict_of_nodes[road[1]] = Node()
            dict_of_nodes[road[0]].children[road[1]] = road[2]
            dict_of_nodes[road[1]].children[road[0]] = road[2]


        return self.go_from_graph(1, dict_of_nodes)

    def go_from_graph(self, node: int, dict_of_nodes) -> int:
        # вернуть min из всех путей, и из путей из путей, пока от ноды путь not passed
        if not dict_of_nodes[node].children:
            return 32767
        else:
            list_of_length = []
            list_of_child = []

            for child in dict_of_nodes[node].children.keys():
                list_of_length.append(dict_of_nodes[node].children[child])
                list_of_child.append(child)

            for child in list_of_child:
                dict_of_nodes[node].children.pop(child)

            for child in list_of_child:
                list_of_length.append(self.go_from_graph(child, dict_of_nodes))

            return min(list_of_length)

def main():
    a = Solution()
    print(a.minScore(14, [[2,9,2308],[2,5,2150],[12,3,4944],[13,5,5462],[2,10,2187],[2,12,8132],[2,13,3666],[4,14,3019],[2,4,6759],[2,14,9869],[1,10,8147],[3,4,7971],[9,13,8026],[5,12,9982],[10,9,6459]]))


if __name__ == '__main__':
    main()
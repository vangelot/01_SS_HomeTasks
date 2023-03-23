class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        list_of_islands = []
        while connections:
            list_of_islands.append(set(connections[0]))
            del connections[0]

            rest = set()
            for conn in connections:
                rest = rest.union(set(conn))

            while list_of_islands[-1] & rest:
                for conn in connections:
                    if (conn[0] in list_of_islands[-1]) or (conn[1] in list_of_islands[-1]):
                        list_of_islands[-1] = list_of_islands[-1].union(set(conn))
                        connections.remove(conn)
                rest = set()
                for conn2 in connections:
                    rest = rest.union((set(conn2)))

        num_of_islands = len(list_of_islands)

        used_comp = set()
        for i in range(len(list_of_islands)):
            used_comp = used_comp.union(list_of_islands[i])

        for i in range(n):
            if i not in used_comp:
                num_of_islands += 1

        return num_of_islands - 1
def main():
    a = Solution()
    print(a.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))


if __name__ == '__main__':
    main()
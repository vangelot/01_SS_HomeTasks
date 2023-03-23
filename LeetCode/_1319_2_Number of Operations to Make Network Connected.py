class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        graph = [set() for i in range(n)]
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)

        seen = [0] * n

        def dfs(i):
            if seen[i] == 1:
                return 0
            seen[i] = 1
            for j in graph[i]:
                dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1


def main():
    a = Solution()
    print(a.makeConnected(5, [[0, 1], [0, 2], [4, 4]]))


if __name__ == '__main__':
    main()
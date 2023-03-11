import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: [ListNode]):
        self.list_of_nodes = []
        while head:
            self.list_of_nodes.append(head)
            head = head.next
        pass

    def getRandom(self) -> int:
        n = random.randrange(len(self.list_of_nodes))
        print(n)
        print(self.list_of_nodes[n].val)
        return self.list_of_nodes[n].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


def main():
    print('hello')
    x = ListNode(1)
    a = Solution(x)
    print(a.getRandom())
    pass


if __name__ == '__main__':
    main()
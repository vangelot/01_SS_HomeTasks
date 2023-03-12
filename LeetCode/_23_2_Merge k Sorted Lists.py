class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: list[[ListNode]]) -> [ListNode]:

        array = []

        for head in lists:
            while head:
                array.append(head.val)
                head = head.next

        array.sort(reverse=True)

        res = None
        for x in array:
            res = ListNode(x, res)

        return res

def main():
    print('hello')
    a = Solution()
    b = ListNode(1)
    b.next = ListNode(7)
    c = ListNode(2)
    c.next = ListNode(4)

    print(a.mergeKLists([b, c]).next.next.val)
    pass


if __name__ == '__main__':
    main()
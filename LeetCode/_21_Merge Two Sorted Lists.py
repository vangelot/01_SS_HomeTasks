class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        while self:
            print(self.val)
            self = self.next
        return ''

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        _list = []
        while list1:
            _list.append(list1.val)
            list1 = list1.next
        while list2:
            _list.append(list2.val)
            list2 = list2.next

        _list.sort(reverse=True)
        if len(_list) == 0:
            return None

        _next = None
        pointer = 0
        while pointer < len(_list):
            res = ListNode(_list[pointer], _next)
            pointer += 1
            _next = res

        return res


def main():
    print('hello')
    a = Solution()
    b = ListNode(1)
    b.next = ListNode(7)
    c = ListNode(2)
    c.next = ListNode(4)

    print(a.mergeTwoLists(b, c))
    print(b)
    pass


if __name__ == '__main__':
    main()
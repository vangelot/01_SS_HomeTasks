class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: list[[ListNode]]) -> [ListNode]:

        res_head = ListNode()
        res_tmp = res_head


        while len(lists) > 0:
            if lists[0]:
                _min = lists[0].val
            else:
                lists.remove(lists[0])
                continue
            print(_min)
            min_index = 0
            head_index = -1
            for head in lists:
                head_index += 1
                if head.val < _min:
                    _min = head.val
                    min_index = head_index
            print('head:', res_head.val)
            res_tmp.next = ListNode(_min)
            res_tmp = res_tmp.next
            if lists[min_index].next:
                lists[min_index] = lists[min_index].next
            else:
                lists.remove(lists[min_index])

        return res_head.next

        pass


def main():
    print('hello')
    a = Solution()
    b = ListNode(1)
    b.next = ListNode(7)
    c = ListNode(2)
    c.next = ListNode(4)

    print(a.mergeKLists([b, c]).next.next.next.next)
    pass


if __name__ == '__main__':
    main()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        was_list = []
        current = head
        while True:
            if current.next is None:
                print('non cycle')
                return None
            elif current in was_list:
                print('cycle')
                return current
            else:
                print('go next')
                was_list.append(current)
                current = current.next
        pass


def main():
    print('hello')
    x = ListNode(10)
    x.next = ListNode(7)
    x.next.next = ListNode(8)
    x.next.next.next = x.next

    a = Solution()
    print(a.detectCycle(x).val)
    pass


if __name__ == '__main__':
    main()
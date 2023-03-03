# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_node(self, num):
        if self.next is None:
            self.next = ListNode(num)
        else:
            self.next.add_node(num)


class Solution:

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        sum = self.str_to_int(self.node_to_str(l1)) + self.str_to_int(self.node_to_str(l2))
        sum_str = str(sum)
        res = ListNode(int(sum_str[len(sum_str)-1]))
        for i in range(1, len(sum_str)):
            res.add_node(int(sum_str[len(sum_str)-i-1]))
        return res

    def node_to_str(self, l: [ListNode]):
        if l.next is None:
            return str(l.val)
        else:
            return str(l.val)+str(self.node_to_str(l.next))
        pass

    def str_to_int(self, _str):
        num = 0
        for i in range(len(_str)):
            num += (int(_str[len(_str)-1-i])) * (10**(len(_str)-i-1))
        return num
    # def addTwoNumbers(self, l1, l2) -> int:
    #     return self.get_number(l1)+self.get_number(l2)
    #
    # def get_number(self, l1):
    #     l1.reverse()
    #     number = 0
    #     for i in range(len(l1)):
    #         number += l1[i] * (10**(len(l1)-1-i))
    #     return number


def main():
    a = Solution()
    b = ListNode(2)
    b.add_node(4)
    b.add_node(3)
    # print(b.val, b.next.val, b.next.next.val)
    c = ListNode(5)
    c.add_node(6)
    c.add_node(4)
    # print(a.node_to_int(b))
    # print(a.str_to_int('211'))
    d = a.addTwoNumbers(b, c)
    print(d.val, d.next.val, d.next.next.val)
    # print(a.get_number([1, 2]))
    pass


if __name__ == '__main__':
    main()
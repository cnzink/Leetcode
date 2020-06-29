# encoding:utf-8
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        print(self.val)
        if self.next:
            self.next.print()

# 暴力解法
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         l3 = ListNode(0)
#         root = l3
#         a = 0
#         b = 0
#         temp = 0
#         while(l1 or l2):
#             root.next = ListNode(0)
#             root = root.next
#             a = l1.val if l1 else 0
#             b = l2.val if l2 else 0
#             root.val = int((a+b+temp)-10 if a+b+temp > 9 else a+b+temp)
#             temp = int((a + b + temp) / 10 if a + b + temp > 9 else 0)
#
#             if l1 :
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
#         if temp != 0:
#             root.next = ListNode(temp)
#         return l3.next

# 好看的答案
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        pre = dummyHead;
        t = 0
        while (l1 != None or l2 != None or t != 0):
            if (l1 != None) :
                t += l1.val
                l1 = l1.next

            if (l2 != None) :
                t += l2.val
                l2 = l2.next

            pre.next = ListNode(t % 10)
            pre = pre.next
            t = int(t/10)
        return dummyHead.next



if __name__ == '__main__':
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # root = l1.next
    # root.next = ListNode(3)
    # root = root.next
    # l1.print()
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # root = l2.next
    # root.next = ListNode(4)
    # root = root.next
    # l2.print()
    l1 = ListNode(5)
    l2 = ListNode(5)
    A = Solution()
    A.addTwoNumbers(l1,l2).print()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m = 0
        n = 0
        i = 0
        j = 0

        while l1:
            h = m
            m = (l1.val * (10 ** i))
            m = m + h
            l1 = l1.next
            i += 1
        while l2:
            f = n
            n = (l2.val * (10 ** j))
            n = n + f
            l2 = l2.next
            j += 1
        z = m + n

        z_str = [int(digit) for digit in str(z)[::-1]]

        def list_to_linked_list(lst):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for value in lst[1:]:
                current.next = ListNode(value)
                current = current.next
            return head

        linked_list = list_to_linked_list(z_str)
        return linked_list

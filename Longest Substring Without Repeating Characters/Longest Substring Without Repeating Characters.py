class ListNode:
    def __init__(self, s=[], next=None):
        self.val = list(s)
        self.next = next


def Find_last(a, arr):
    last_occurrence = {}
    for i in range(len(arr)):
        char = arr[i]
        if i == a:
            last = last_occurrence[arr[i]]
            if last + 1 < len(arr):
                return last + 1
        else:
            last_occurrence[char] = i


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = ListNode()
        current = head
        x = list(s)
        max_len = 0
        current.next = ListNode()
        current = current.next
        i = 0
        while i < len(x):
            if x[i] in current.val:
                if len(current.val) > max_len:
                    max_len = len(current.val)
                i = Find_last(i, x)
                current.next = ListNode()
                current = current.next
                current.val.append(x[i])
                i += 1


            elif x[i]:
                current.val.append(x[i])
                i += 1
                if i == len(x):
                    if len(current.val) > max_len:
                        max_len = len(current.val)


            else:
                i += 1
        return max_len
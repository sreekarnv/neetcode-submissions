# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        tail = d
        carry = 0

        while l1 or l2:
            curr = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = curr // 10 

            tail.next = ListNode(curr % 10)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        tail.next = ListNode(carry) if carry else None

        return d.next
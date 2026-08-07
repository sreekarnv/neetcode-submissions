# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverse(head)
        d = ListNode()
        prev = d
        curr = head
        i = 1

        while curr:
            if i == n:
                prev.next = curr.next
                break
            
            prev.next = curr
            prev = prev.next
            curr = curr.next
            i += 1
        
        return self.reverse(d.next)
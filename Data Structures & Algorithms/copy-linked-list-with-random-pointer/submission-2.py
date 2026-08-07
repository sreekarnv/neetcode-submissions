"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {}
        curr = head

        while curr:
            mapper[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = mapper[curr]
            copy.next = mapper[curr.next] if curr.next else None
            copy.random = mapper[curr.random] if curr.random else None

            curr = curr.next
        
        return mapper[head] if head else None
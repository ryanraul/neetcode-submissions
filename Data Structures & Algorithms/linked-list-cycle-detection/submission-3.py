# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

approach: slow and fast pointers

- slow: moving 1 pointer for each iteration
- fast: moving 2 pointers for each iteration

logic:
- if it has a cycle, always slow and fast pointer will
    - collide at certain time 


while fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False

    

"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""

- [0,1,2,3]


reverse(before, current)
    if(current is None):
        return

    reverse(current, current.next)
    current.next = before


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_begin = None
        def reverse(before, current):
            if current is None:
                return before
            
            new_begin = reverse(current, current.next)
            current.next = before
            return new_begin
        
        new_begin = reverse(None, head)
        print(new_begin)
        return new_begin
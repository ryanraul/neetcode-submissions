# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
 l       r
[0,1,2,3,4]

[0,1,2,3,4]
a = 4


aux = head[r]
head[r] = head[l]
head[l] = aux

[None, N(0, N(1))]
[N(0), N(1, N(2))]
[N(1), N(2, N(3))]
[N(2), N(3, none)]
[N(3), none]

[N(3), N(2)]
[N(2), N(1)]
[N(1), N(0)]
[N(0), none]

reverseLinked(previous, current)
    if current is None:
        return

    reverseLinked(current, current.next)
    current.next = previous

"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseNode(previous, current):
            if current is None:
                return previous

            new_beginning = reverseNode(current, current.next)
            current.next = previous
            
            return new_beginning
        
        return reverseNode(None, head)

        
        
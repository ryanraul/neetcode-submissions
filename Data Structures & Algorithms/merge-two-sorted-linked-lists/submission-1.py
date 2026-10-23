# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

[1,2,4]
[1,3,5]

 1 <= 1
 n1.next = merge(n1.next, n2) = 1
 return n1 = 1

 2 <= 1
 n2.next = merge(n1, n2.next) = 2
 return = n2 = 1

 2 <= 3
 n1.next = merge(n1.next, n2) = 3
 return n1 = 2

 4 <= 3
 n2.next = merge(n1, n2.next) = 4
 reuturn = n2 = 3
 
 4 <= 5
 n1.next = merge(n1.next, n2) = 5
 return n1 = n4 = 4

 None
 return n2 = 5

 

 
merge(n1, n2)

    if n1 <= n2:
        l1.next = merge(n1.next, n2)
        return l1
    else:
        l2.next = merget(n1, n2.next)
        merge()
    
    merge

"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
        def merge(n1, n2):
            if n1 is None:
                return n2
            if n2 is None:
                return n1

            if n1.val <= n2.val:
                n1.next = merge(n1.next, n2)
                return n1
            else:
                n2.next = merge(n1, n2.next)
                return n2

        return merge(list1,list2)    
        
        
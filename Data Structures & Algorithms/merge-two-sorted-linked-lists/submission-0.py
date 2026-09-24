# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
list1 = [1,2,4]
list2 = [1,3,5]

- if l1 node is less or equal than l2 node
    - merge_list.next = l1

while l1 is not None or l2 is not None:

    if l1 is None:
        l3.next = l2
        break
    else:
        l3.next = l1
        break

    if l1.val <= l2.val:
        l3.next = l1
        l1 = l1.next
    else:
        l3.next = l2
        l2 = l2.next


"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        def merge_list(l3, l1, l2):
            if l1 is None:
                l3.next = l2
                return
            elif l2 is None:
                l3.next = l1
                return

            if l1.val <= l2.val:
                l3.next = l1
                merge_list(l3.next, l1.next, l2)
            else:
                l3.next = l2
                merge_list(l3.next, l1, l2.next)

        if list1.val <= list2.val:
            l3 = list1
            merge_list(l3, list1.next, list2)
        else:
            l3 = list2
            merge_list(l3, list1, list2.next)

        return l3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(-1)   # dummy node
        merge = dummy          # pointer to build the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                merge.next = list1
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
            merge = merge.next   # advance merge pointer

        # Attach the remaining nodes
        if list1:
            merge.next = list1
        else:
            merge.next = list2

        return dummy.next   # return head of merged list

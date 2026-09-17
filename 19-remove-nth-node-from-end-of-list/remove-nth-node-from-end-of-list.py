# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)   # dummy node before head
        dummy.next = head

        front = dummy
        back = dummy

        # Move front pointer n+1 steps ahead
        for _ in range(n + 1):
            front = front.next

        # Move both pointers until front reaches end
        while front:
            front = front.next
            back = back.next

        # Skip the nth node from end
        back.next = back.next.next

        return dummy.next   # return new head

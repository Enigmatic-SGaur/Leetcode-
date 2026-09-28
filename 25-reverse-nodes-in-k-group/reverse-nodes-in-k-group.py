# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        ktail = None
        newHead = None

        while ptr:
            count = 0
            ptr = head

            # Check if there are at least k nodes left
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            if count == k:
                # Reverse k nodes
                revHead = self.reverseLinkedList(head, k)

                if newHead is None:
                    newHead = revHead

                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr

        if ktail:
            ktail.next = head

        return newHead if newHead else head

    def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
        newHead = None
        ptr = head

        while k > 0:
            nextNode = ptr.next
            ptr.next = newHead
            newHead = ptr
            ptr = nextNode
            k -= 1

        return newHead

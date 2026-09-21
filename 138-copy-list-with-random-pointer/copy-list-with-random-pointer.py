class Solution:
    def __init__(self):
        self.visitedNode = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        if head in self.visitedNode:
            return self.visitedNode[head]

        # Create a new node with the same value
        node = Node(head.val, None, None)

        # Store the newly created node in the visited dictionary
        self.visitedNode[head] = node

        # Recursively copy the next and random pointers
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

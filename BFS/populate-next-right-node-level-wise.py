# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque()
        q.append(root)
        while(q):
            prevNode = None
            levelSize = len(q)
            for _ in range(levelSize):
                currNode = q.popleft()
                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        
        return root

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        if not root:
            return result
        q = deque()
        q.append(root)
        leftToRight = True
        while q:
            levelSize = len(q)
            currLevel = deque()
            for _ in range(levelSize):
                currNode = q.popleft()
                if leftToRight:
                    currLevel.append(currNode.val)
                else:
                    currLevel.appendleft(currNode.val)
                if (currNode.left):
                    q.append(currNode.left)
                if (currNode.right):
                    q.append(currNode.right)
            result.append(list(currLevel))
            leftToRight = not leftToRight
        return result
            
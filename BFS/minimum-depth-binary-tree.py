# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root is None:
            return res
        q = deque()
        q.append(root)
        while(q):
            levelSize = len(q)
            res+=1
            for _ in range(levelSize):
                currNode = q.popleft()
                if not currNode.left and not currNode.right:
                    return res
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        return res     
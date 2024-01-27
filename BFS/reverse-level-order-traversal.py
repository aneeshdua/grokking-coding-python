# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque()
        res=[]
        q.append(root)
        while q:
            currLvl = []
            lvlSize = len(q)
            for _ in range(lvlSize):
                currNode = q.popleft()
                currLvl.append(currNode.val)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            res.insert(0,currLvl)
        return res
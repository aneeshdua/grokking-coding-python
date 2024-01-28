# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return 0
        q = deque()
        q.append(root)
        while(q):
            levelSum = 0
            levelSize = len(q)
            for _ in range(levelSize):
                currNode = q.popleft()
                levelSum +=currNode.val
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            res.append(levelSum/levelSize)
        return res
# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while(q):
            levelSize = len(q)
            for i in range(levelSize):
                currNode = q.popleft()
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                if i == levelSize-1:
                    res.append(currNode.val)
        return res                
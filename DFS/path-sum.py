# https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def foo(node,currSum):
            if not node:
                return False
            newSum = currSum + node.val
            if newSum == targetSum and not node.left and not node.right:
                return True
            else:
                return foo(node.left,newSum) or foo(node.right,newSum)
        if not root:
            return False
        currSum=0
        return foo(root,currSum)
        
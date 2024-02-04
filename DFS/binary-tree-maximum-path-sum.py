# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.globalMaxPathSum = float('-inf')  # Rename the class attribute

    def dfs_path_sum(self, root):
        if not root:
            return 0

        left = self.dfs_path_sum(root.left)
        right = self.dfs_path_sum(root.right)

        left = max(left, 0)  # ignore negative sums
        right = max(right, 0)  # ignore negative sums

        localMaxima = left + right + root.val
        self.globalMaxPathSum = max(self.globalMaxPathSum, localMaxima)

        return max(left, right) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs_path_sum(root)
        return self.globalMaxPathSum  # Use the renamed class attribute

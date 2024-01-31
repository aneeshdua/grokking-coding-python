# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root,targetSum,[],res)
        return res

    def dfs(self,root,sum,path,res):
        if(root):
            if not root.left and not root.right and sum==root.val:
                path.append(root.val)
                res.append(path)
            self.dfs(root.left,sum-root.val,path+[root.val],res)
            self.dfs(root.right,sum-root.val,path+[root.val],res)
            
# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths(node,targetSum,currPath):
            if not node:
                return 0
            currPath.append(node.val)
            pathCount,pathSum = 0,0
            for i in range(len(currPath)-1,-1,-1):
                pathSum += currPath[i]
                if pathSum ==targetSum:
                    pathCount +=1
            
            pathCount += count_paths(node.left,targetSum,currPath)
            pathCount += count_paths(node.right,targetSum,currPath)

            del currPath[-1]

            return pathCount
        
        return count_paths(root,targetSum,[])
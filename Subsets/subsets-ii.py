# https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list.sort(nums)
        subsets=[]
        subsets.append([])
        startIndex,endIndex = 0,0
        for j in range(len(nums)):
            startIndex = 0
            if j>0 and nums[j]==nums[j-1]:
                startIndex = endIndex+1
            endIndex = len(subsets)-1
            for i in range(startIndex,endIndex+1):
                tmpSet = list(subsets[i])
                tmpSet.append(nums[j])
                subsets.append(tmpSet)
        return subsets

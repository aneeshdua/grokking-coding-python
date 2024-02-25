# https://leetcode.com/problems/subsets/description/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for currNum in nums:
            n = len(subsets)
            for i in range(n):
                tmpSet = list(subsets[i])
                tmpSet.append(currNum)
                subsets.append(tmpSet)
        return subsets
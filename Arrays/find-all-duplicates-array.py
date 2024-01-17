# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i+=1
        duplicates = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                duplicates.append(nums[i])
        return duplicates
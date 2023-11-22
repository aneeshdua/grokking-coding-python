# 3sum smaller leetcode locked
"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        resCount = 0
        for i in range(0,len(nums)-2):
            newTarget = target - nums[i]
            left = i+1
            right = len(nums)-1
            while(left<right and right<len(nums)):
                if nums[left]+nums[right]<newTarget:
                    resCount+=(right-left)
                    left+=1
                else:
                    right-=1
        

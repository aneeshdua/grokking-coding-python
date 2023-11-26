# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1

        while(low<len(nums)-1 and nums[low]<=nums[low+1]):
            low+=1
        
        if low == len(nums)-1:
            return 0
        
        while(high>0 and nums[high]>=nums[high-1]):
            high-=1
        
        subArrayMax = float('-inf')
        subArrayMin = float('inf')
        for k in range(low,high+1):
            subArrayMax = max(subArrayMax,nums[k])
            subArrayMin = min(subArrayMin,nums[k])

        while low>0 and nums[low-1]>subArrayMin:
            low-=1
        
        while high<len(nums)-1 and nums[high+1]<subArrayMax:
            high+=1
        
        return high-low+1
        

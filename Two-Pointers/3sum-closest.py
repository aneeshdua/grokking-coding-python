# https://leetcode.com/problems/3sum-closest/submissions/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minDiff = float('inf')
        resSum = 0
        nums = sorted(nums)
        size = len(nums)
        for i in range(len(nums)-2):
            curr_fixed = nums[i]
            low = i+1
            high = size-1
            while(low<high):
                curr_sum = nums[low]+nums[high]+curr_fixed
                if minDiff > abs(curr_sum-target):
                    minDiff = abs(curr_sum-target)
                    resSum = curr_sum
                if curr_sum == target:
                    return target
                elif curr_sum >target:
                    high -=1
                else:
                    low+=1
            
        return resSum
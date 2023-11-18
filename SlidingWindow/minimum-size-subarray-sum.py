# https://leetcode.com/problems/minimum-size-subarray-sum/editorial/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        totalSum = 0
        for num in nums:
            if num == target:
                return 1
            totalSum += num
        if totalSum<target:
            return 0
        elif totalSum == target:
            return len(nums)
        res = float('inf')
        left=0
        currSum=0
        for i in range(0,len(nums)):
            currSum += nums[i]
            while(currSum>=target):
                res = min(res,i+1-left)
                currSum -= nums[left]
                left += 1
        if res != float('inf'):
            return res
        else:
            return 0


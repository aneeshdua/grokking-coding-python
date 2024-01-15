# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = (0+len(nums))*(len(nums)+1)//2
        for i in range(len(nums)):
            expected -= nums[i]
        return expected
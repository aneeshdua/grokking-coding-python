#https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxOnes=0
        # windowStart=0
        # maxLength=0
        # for windowEnd in range(len(nums)):
            # if nums[windowEnd]==1:
            #     maxOnes+=1
            # if windowEnd-windowStart+1-maxOnes > k:
            #     if nums[windowStart] ==1:
            #         maxOnes-=1
            #     windowStart+=1
            # maxLength = max(maxLength,windowEnd-windowStart+1)
        # return maxLength
        windowStart=0
        maxLength=0
        zeroCounter=0
        for windowEnd in range(len(nums)):
            if nums[windowEnd]==0:
                zeroCounter+=1
            while(zeroCounter>k):
                if nums[windowStart]==0:
                    zeroCounter-=1
                windowStart+=1
            maxLength = max(maxLength,windowEnd-windowStart+1)
        return maxLength
#https://leetcode.com/problems/subarray-product-less-than-k/description/
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], target: int) -> int:
        if target <= 1: return 0
        #result=[]
        count=0
        product=1
        left=0
        for right in range(0,len(nums)):
            product *= nums[right]
            while(product>=target and left< len(nums)):
                product = product/nums[left]
                left+=1
            count += (right-left+1)
            # To get all triplets
            # templist = []
            # for i in range(right,left-1,-1):
            #     templist.insert(0,nums[i])
            #     result.append(templist)
        return count
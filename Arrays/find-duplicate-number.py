# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find the intersection point of the two runners.
        # tortoise = hare = nums[0]
        # while True:
        #     tortoise = nums[tortoise]
        #     hare = nums[nums[hare]]
        #     if tortoise == hare:
        #         break
        
        # # Find the "entrance" to the cycle.
        # tortoise = nums[0]
        # while tortoise != hare:
        #     tortoise = nums[tortoise]
        #     hare = nums[hare]
        i=0
        while i <len(nums):
            if nums[i] != i+1:
                j = nums[i]-1
                if nums[i] != nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                else:
                    return nums[i]
            else:
                i+=1
        return -1


        
        return hare
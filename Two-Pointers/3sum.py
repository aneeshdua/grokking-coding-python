#https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3: # deal with special input
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [sorted(nums)]

        size=len(nums)
        res = []
        nums = sorted(nums) # sorted, O(nlgn)
        for i in range(size-2):
            if(i==0 or (i>0 and nums[i]!=nums[i-1])):
                curr_target = -1*nums[i]
                low=i+1
                high=size-1
                while(low<high):
                    if(nums[low]+nums[high]==curr_target):
                        res.append([nums[i],nums[low],nums[high]])
                        while(low<high and nums[low] == nums[low+1]):
                            low+=1
                        while(low<high and nums[high] == nums[high-1]):
                            high-=1
                        low+=1
                        high-=1
                        #break
                    elif(nums[low]+nums[high]>curr_target):
                        high-=1
                    else:
                        low+=1
        return res

            
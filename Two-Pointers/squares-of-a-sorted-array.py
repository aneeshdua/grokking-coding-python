# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        resArr = [0 for i in range(len(nums))]
        left=0
        right=len(nums)-1
        highestId = len(nums)-1
        while(left<=right):
            leftSquare = nums[left]*nums[left]
            rightSquare = nums[right]*nums[right]
            if(leftSquare>rightSquare):
                resArr[highestId] = leftSquare
                left+=1
            else:
                resArr[highestId] = rightSquare
                right-=1
            highestId-=1
        return resArr
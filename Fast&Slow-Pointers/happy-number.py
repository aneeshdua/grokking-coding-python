# https://leetcode.com/problems/happy-number/submissions/
class Solution:
    def findSquareSum(self,n):
        result=0
        while n>0:
            last = n%10
            result += last*last
            n = n//10
        return result 

    def isHappy(self, n: int) -> bool:
        slow = self.findSquareSum(n)
        fast = self.findSquareSum(self.findSquareSum(n))
        while(slow !=fast and fast != 1):
            slow = self.findSquareSum(slow)
            fast = self.findSquareSum(self.findSquareSum(fast))

        return fast==1

    
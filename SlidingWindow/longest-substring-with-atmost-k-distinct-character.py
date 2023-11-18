#LEetcode 340
"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""
class Solution:
    def LongestSubstringKDistinct(self, k: int, inputStr: str) -> int:
        windowStart=0
        maxLength=0
        seenMap = {}
        for windowEnd in range(0,len(inputStr)):
            seenMap[inputStr[windowEnd]] = inputStr.get(windowEnd,0)+1
            while len(seenMap)>k:
                seenMap[windowStart] -=1
                if seenMap[windowStart]==0:
                    del seenMap[windowStart]
                windowStart+=1
            maxLength = max(maxLength,windowEnd-windowStart+1)
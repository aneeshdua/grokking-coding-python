# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        maxLength=0
        windowStart=0
        for windowEnd in range(len(s)):
            if(s[windowEnd] not in charMap):
                #already present - repeating
                maxLength = max(maxLength,windowEnd-windowStart+1)
            else:
                if charMap[s[windowEnd]]<windowStart:
                    maxLength = max(maxLength,windowEnd-windowStart+1)
                else:
                    windowStart = charMap[s[windowEnd]]+1
            charMap[s[windowEnd]] = windowEnd    
        return maxLength

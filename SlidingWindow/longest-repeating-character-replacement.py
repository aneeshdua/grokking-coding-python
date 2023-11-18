#https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart=0
        maxLength=0
        maxRepeatLetterCount=0
        charMap={}
        for windowEnd in range(len(s)):
            charMap[s[windowEnd]] = charMap.get(s[windowEnd],0)+1
            maxRepeatLetterCount = max(maxRepeatLetterCount,charMap[s[windowEnd]])
            if (windowEnd-windowStart+1 - maxRepeatLetterCount > k):
                charMap[s[windowStart]]-=1
                windowStart+=1
            
            maxLength = max(maxLength,windowEnd-windowStart+1)
        return maxLength
        # currentChar = s[0]
        # maxLength=0
        # windowStart=0
        # windowEnd=0
        # replacements=0
        # checkpoint=0
        # while windowEnd< len(s):
            
        #     if(s[windowEnd])==currentChar:
        #         windowEnd+=1
        #         maxLength = max(maxLength, windowEnd-windowStart+1)
        #     else:
        #         if replacements <k:
        #             checkpoint=windowEnd
        #             replacements+=1
        #             windowEnd+=1
        #             maxLength = max(maxLength, windowEnd-windowStart+1)
        #         else:
        #             replacements=0
        #             windowEnd = checkpoint
        #             windowStart = checkpoint
        #             currentChar = s[checkpoint]
        # return maxLength

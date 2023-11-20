#https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >len(s2):
            return False
        s1Map = [0 for i in range(26)]
        s2Map = [0 for i in range(26)]

        for i in range (len(s1)):
            s1Map[ord(s1[i])-97]+=1
            s2Map[ord(s2[i])-97]+=1
        
        for i in range(0,len(s2)-len(s1)):
            if s1Map == s2Map:
                return True
            #print(ord(s2[i+len(s1)])-97)
            s2Map[ord(s2[i+len(s1)])-97]+=1
            s2Map[ord(s2[i])-97]-=1

        return s1Map == s2Map
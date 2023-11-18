# https://leetcode.com/problems/fruit-into-baskets/description/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitMap = {}
        windowStart=0
        maxLength=0
        for windowEnd in range(0,len(fruits)):
            fruitMap[fruits[windowEnd]]= fruitMap.get(fruits[windowEnd],0)+1
            while(len(fruitMap)>2):
                fruitMap[fruits[windowStart]]-=1
                if fruitMap[fruits[windowStart]] ==0:
                    del fruitMap[fruits[windowStart]]
                windowStart+=1
            maxLength = max(maxLength,windowEnd-windowStart+1)

        return maxLength
            

# https://leetcode.com/problems/interval-list-intersections/description/
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []

        i=0
        j=0
        result = []
        while(i<len(firstList) and j<len(secondList)):
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])

            if l <= r :
                result.append([l, r])
            # if (firstList[i][0] > secondList[j][0] and firstList[i][0] <= secondList[j][1]) or (secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]):
            #     result.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
            if (firstList[i][1]<secondList[j][1]):
                i+=1
            else:
                j+=1
                
        return result
            
        
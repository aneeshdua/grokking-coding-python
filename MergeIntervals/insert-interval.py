#https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == None or intervals == []:
            return [newInterval]

        result = []
        i=0

        #fast forward outside of scope intervals
        while(i<len(intervals) and intervals[i][1]<newInterval[0]):
            result.append(intervals[i])
            i+=1

        #merge all intervals that overlap
        while(i<len(intervals) and intervals[i][0] <=newInterval[1]):
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i+=1
        
        result.append(newInterval)

        result = result + intervals[i:]

        return result
                


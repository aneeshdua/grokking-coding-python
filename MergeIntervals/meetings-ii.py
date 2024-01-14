"""
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.
"""
# LEetcode meetings 2
from heapq import heapify, heappush, heappop
from typing import List

def meetingsii(meetings: List[List[int]]) -> int:
    meetings = sorted(meetings,key = lambda x:x[0])
    activeMeetings = [] 
    heapify(activeMeetings) 
    count=0
    for i in range(len(meetings)):
        # remove all meetings that have ended
        while(len(activeMeetings) !=0 and meetings[i][0]>=activeMeetings[0]):
            heappop(activeMeetings)
        # add current meeting to the heap
        heappush(activeMeetings,meetings[i][1])
        # get max active meeting count
        count = max(count,len(activeMeetings))
    return count


print(meetingsii([[1,4],[2,3],[3,6]]))

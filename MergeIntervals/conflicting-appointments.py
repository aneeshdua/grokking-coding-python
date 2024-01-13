"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
"""
class Solution:
    # def compare(item1, item2):
    #     if item1[0] < item2[0]:
    #         return -1
    #     elif item1[0] > item2[0]:
    #         return 1
    #     else:
    #         return 0
    def check_conflict(self, intervals: List[List[int]]) -> boolean:
        intervals = sorted(intervals,key=lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]> intervals[i+1][0]:
                return False
        return True
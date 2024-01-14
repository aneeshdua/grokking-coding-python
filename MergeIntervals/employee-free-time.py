"""
For ‘K’ employees, we are given a list of intervals representing the working hours of
each employee. Our goal is to find out if there is a free interval that is common to 
all employees.You can assume that each list of employee working hours is sorted 
on the start time.
"""

from heapq import heapify,heappush,heappop
from typing import List

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

def getFreeTime(employees: List[List[Interval]]) -> int:
    # Flattening the schedule
    intervals = [interval for employee in employees for interval in employee]
    # Sorting by start of each Interval
    intervals.sort(key=lambda x: x.start)
    res, end = [], intervals[0].end
    # Checking for free time between intervals
    for i in intervals[1:]:
        if end < i.start:
            res.append([end, i.start])
        end = max(end, i.end)
    return res

                    

emp_list = [
    [Interval(1,3),Interval(5,6)],
    [Interval(2,3),Interval(6,8)]
]

print(getFreeTime(emp_list))

"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
"""

from heapq import heapify,heappush,heappop
from typing import List

class Job:
    def __init__(self,start,end,load):
        self.start = start
        self.end = end
        self.load = load

    # Operator overloading for the
    # Object that is Job
    def __lt__(self, other):
 
        # min heap based on job.end
        return self.end < other.end

def max_cpu_load(processes: List[Job]) -> int:
    processes= sorted(processes, key = lambda x:x.start)
    maxLoad = 0
    currLoad=0
    minHeap = []
    #heapify(minHeap)
    for p in processes:
        # remove all jobs that have ended
        while(len(minHeap)>0 and p.start>minHeap[0].end):
            currLoad -= minHeap[0].load
            heappop(minHeap)            

        # add the current job to the minHeap
        heappush(minHeap,p)

        currLoad += p.load
        maxLoad = max(maxLoad,currLoad)
    
    return maxLoad


job_list = [
        Job(2, 4, 5),
        Job(0, 6, 7),
        Job(5, 10, 6),
        Job(0, 3, 10)
    ]
jobs = [Job(1, 4, 3), Job(2, 5, 4),
            Job(7, 9, 6)]
print(max_cpu_load(jobs))

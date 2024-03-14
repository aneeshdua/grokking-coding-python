"""
1 . what does put do? stores the element and curr system timestamp?
2. get_Count returns count of timestamps that are currently valid ?
3. get_total_count - returns total number of elements in the object? 
4. Each put operation will be at 1 per second?
"""

import time

class Counter:
    def __init__(self):
        self.store = {}
    
    def put(self,key):
        if key in self.store:
            self.store[key].append(time.time()+300)
        else:
            self.store[key] = [time.time()+300]
    
    def get_count(self,key):
        if key not in self.store:
            return 0
        remove_invalid_timestamps(self.store[key])
        # while(index<len(self.store[key]) and self.store[key][index]<currTime):
        #     index+=1
        # #remove the invalid
        # self.store[key] = self.store[key][index:]
        return len(self.store[key])

    def get_total_count(self):
        count=0
        for key,value in self.store.items():
            remove_invalid_timestamps(value)
            if len(value)>0:
                count+=1
        return count
        

def remove_invalid_timestamps(arr):
    #sorted array
    currTime = time.time()
    # index=0
    # while(index<len(arr) and arr[index]<currTime):
    #     index+=1
    # arr = arr[index:]
    low = 0
    high = len(arr)

    while(low<high):
        mid = low+(high-low)//2
        if arr[mid] > currTime:
            high = mid-1
        elif arr[mid]<currTime:
            low = mid+1
        else:
            break # assuming 1 request per second
    return mid



if __name__ == "main":

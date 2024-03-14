"""
Req:
1. List of tasks
2. Each task may or may not have a dependency
3. Implement a system to execute all tasks in optimal time
"""
import time
from collections import Counter

class Task:
    def __init__(self,name:str,timeout:int,dependencyTasks:list[str]):
        self.name = name
        self.timeout = timeout
        self.dependencyTasks = dependencyTasks
        self.isStarted = False
        self.isComplete = False
    
    def __repr__(self):
        return f"<Task name:{self.name} isComplete:{self.isComplete} isStarted:{self.isStarted}>"

def runTasks(job: set[Task]):
    #Iterate over all tasks and start which have no dependency
    #Add all jobs running to a run Queue
    #Periodicaly check if each job has completed its time
    runQueue = Counter()
    completedCount=0
    for task in job.values():
        if len(task.dependencyTasks)==0:
            runQueue[task.name] = time.time()+task.timeout
            print("Task added to RunQueue:", task.name)
            task.isStarted = True
    print(runQueue)
    #Do remaining tasks
    while completedCount<len(job):
        print("completedCount",completedCount)
        for task in job.values():
            currTime = time.time()
            if task.isComplete == False:
                if task.isStarted:
                    if currTime>=runQueue[task]:
                        print("Task completed:", task.name)
                        task.isComplete = True
                        completedCount+=1
                        del runQueue[task.name]
                        for otherTask in job.values():
                            if task.name in otherTask.dependencyTasks:
                                # print(task.name,otherTask, otherTask.dependencyTasks)
                                otherTask.dependencyTasks.remove(task.name)
                else:
                    if len(task.dependencyTasks)==0:
                        runQueue[task.name] = time.time()+task.timeout
                        print("Task added to RunQueue:", task.name)
                        task.isStarted = True
                
            time.sleep(1)
    print("Jobs complete")
    return

a = Task('A',3,[])
b = Task('B',1,[])
c = Task('C',1,[])
d = Task('D',2,['A','B'])
e = Task('E',4,['D','C'])
job = {
    'A': a,
    'B': b,
    'C': c,
    'D': d,
    'E': e
}

runTasks(job)

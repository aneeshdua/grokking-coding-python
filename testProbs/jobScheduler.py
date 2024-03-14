"""
tasks:-
1. Name
2. DependencyTasks

Each tasks takes x amount of time
Interface vs Classes??

Assumptions:
1. Time is given in seconds
"""
import time

class Task:
    def __init__(self,name:str,dependencyTasks:list['Task'],time:int):
        self.name = name
        self.dependencyTasks = dependencyTasks
        self.time = time
        self.isComplete = False # default
        self.followingTasks = []

    def register_downstream_job(self, task):
        self.followingTasks.append(task)

runQueue={}

def run (task: Task):
    print("Running Task", task.name)
    # Add task to runQueue
    #Run the task
    #Remove the task from runQueue
    #Run downnstream jobs
    runQueue[task.name] = time.time()+task.time
    time.sleep(task.time)
    del runQueue[task.name]
    if len(task.followingTasks) >0:
        for d in task.followingTasks:
            run(d)
    return 
def runTasks(tasks:list[Task]):
   
    # completedCount=0
    # totalTasks = len(tasks)
    # runQueue = {}
    # while completedCount<totalTasks:
    #     for t in tasks:
    #         if t.isComplete:
    #             continue
    #         if len(t.dependencyTasks)==0:
    #             runQueue[t.name] = t.time+time.time()
    #         else:
    #             for d in t.dependencyTasks:
    #                 if d in runQueue and runQueue[]





a = Task('A',[],3,)
b = Task('B',[],2)
c = Task('C',[],1)

d = Task('D',[a,b],3)
e = Task('E',[d,c],2)

a.register_downstream_job(d)
b.register_downstream_job(d)

d.register_downstream_job(e)
c.register_downstream_job(e)

runTasks([a,b,c,d,e])
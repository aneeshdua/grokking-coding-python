import time

class Task:
    def __init__(self,name,time):
        self.name = name
        self.followingTasks = []
        self.dependencyTasks = []
        self.time = time
    
    def addFollowingTasks(self,t):
        self.followingTasks.append(t)

    def addDependencyTasks(self,t):
        self.dependencyTasks.append(t)

    def getDependencyList(self):
        for task in self.dependencyTasks:
            print(task.name)
    
    def runTask(self):
        print("Current processing: ", self.name)
        if self.dependencyTasks == []:
            print("Running Task",self.name)
            time.sleep(self.time)# running the task
            for task in self.followingTasks:
                print("FollowingTask",task.name)
                task.dependencyTasks.remove(self)
                task.getDependencyList()
                task.runTask()
        else:
            print("Waiting for dependency Tasks to finish")


a = Task('A',1)
b = Task('B',1)
c = Task('C',1)
d = Task('D',1)
e = Task('E',1)

d.addDependencyTasks(a)
d.addDependencyTasks(b)

e.addDependencyTasks(d)
e.addDependencyTasks(c)

a.addFollowingTasks(d)
b.addFollowingTasks(d)
d.addFollowingTasks(e)
c.addFollowingTasks(e)

a.runTask()
b.runTask()
c.runTask()
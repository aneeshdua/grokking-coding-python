import threading
import time

class Job:
    def __init__(self, name):
        self.name = name
        self.upstream_jobs = []
        self.downstream_job = None

    def register_upstream_job(self, job):
        self.upstream_jobs.append(job)
        job.register_downstream_job(self)

    def register_downstream_job(self, job):
        self.downstream_job = job

    def run(self):
        if self.upstream_jobs:
            print(f"Waiting for upstream jobs to complete for {self.name}")
            for job in self.upstream_jobs:
                job.run()
        else:
            def delayed_run():
                time.sleep(1)
                print(f"Completed job {self.name}")
                if self.downstream_job:
                    self.downstream_job.run()
                else:
                    print("Jobs complete")

            threading.Thread(target=delayed_run).start()

a = Job('a')
b = Job('b')
c = Job('c')
d = Job('d')
e = Job('e')
#need to register downstream jobs
a.register_downstream_job(d)
b.register_downstream_job(d)

d.register_downstream_job(e)
c.register_downstream_job(e)


d.register_upstream_job(a)
d.register_upstream_job(b)
e.register_upstream_job(d)
e.register_upstream_job(c)


def run_tasks():
    a.run()
    b.run()
    c.run()

run_tasks()

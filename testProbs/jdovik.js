class Job {
    constructor(name) {
        this.name = name
        this.upstreamJobs = [];
        this.downstreamJob = null;
    }

    registerUpstreamJob(job){
        this.upstreamJobs.push(job);
        job.registerDownstreamJob(this);
    }
    registerDownstreamJob(job){
        this.downstreamJob = job;
    }

    run(job){
        console.log("Job arguement: ",job)
        const jobIdx = this.upstreamJobs.indexOf(job);
        this.upstreamJobs.splice(jobIdx,1)
        if (this.upstreamJobs.length===0){
            setTimeout(()=>{
                console.log(`completed job ${this.name}`);
                if (this.downstreamJob) {
                    console.log("this.downstreamJob", this.downstreamJob);
                    this.downstreamJob.run(this);
                } else {
                    console.log("Jobs complete");
                }
            },1000);
        }
    }
}

const a = new Job('a')
const b = new Job('b')
const c = new Job('c')
const d = new Job('d')
// const e = new Job('e')

d.registerUpstreamJob(a);
d.registerUpstreamJob(b);
// e.registerUpstreamJob(d);
// e.registerUpstreamJob(c);

const runTasks = ()=> {
    a.run();
    b.run();
    // c.run();
}

runTasks()
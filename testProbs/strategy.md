My LC Prep strategy:
- Pattern: You should know all LC patterns. Plus should be able to code them fluently. This requires repeated practise on already solved problems. I used to solve the same problem mutliple times and repeated across days, mentally and physically. This helped not to forget the pattern and code template. 
- Approach: When to use which pattern is what I call approach. It requires step by step process of problem solving to understand which underlying pattern(CS Data structure and algorithm) is being used. Like if the problem asks for multiple scans on entire array for each element, its quadratic solution. The bottleneck is repeated scan. Check if I can solve it by single scan. For this, I can use a HashMap / prefix sum. If for each element, I need to access all precious elements in order of last accessed, I need to chain them using a stack. If problem asks for largest subarray length, check what all indices can be start of poasible subarrays. And for each start, if its an monotonically sorted array, check logarithmically for possible ends.
- Timed practise with talking out loud: Did LC daily challenge, mocks with discord candidates, LC contests.

lld: 
- Design dsa type problems (all companies favourite): Mutli DS combo is the requirement. Like mix of hashmap and treemap in topK frequent pattern.
- Concurrency questions (Uber favourite): like Job scheduler, message queue (push and pull), print odd even 
- Machine coding for 2 hours: design patterns, SOLID, custom exception expected (eg: flipkart)
- Machine coding for 1 hour: in which design pattern could be used, but only if you have time

HLD: You just gotta know all the questions in grokking / alexxu breadth wise. Plus company specific favuorite questions like Uber asks lot about proximity service and heatmap. DDIA is really helpful but only after completely all grokking questions. 
I coupled DDIA replication and sharding chapters with Mongodb and cassandra internal working which was very helpful in interviews. Plus do a lot of mocks. Be the interviewer during mocks, and ask questions to SDE3s or Staffs. Helps to see how seniors think and organize systems knowledge in 1 hour.

Behavioural:
Write down major projects or tasks of all previous companies and arrange their points according to Amazon principles. Plus get SDE3s/Staffs/EMs/CTOs to take your mock interview and ask for feedback.

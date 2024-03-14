def largestSubstring(s,k):
    n = len(s)
    if n==0 or n<k:
        return ""
    res = ""
    curr = 0
    start = 0
    print("Iteration: ",k)
    while(k>0):
        end = n-k
        curr = max(s[start:end+1])
        print("start",start, end='\t')
        print("end+1",end+1, end='\t')
        print("curr",curr, end='\t')
        start += s[start:].index(curr)+1
        
        res = res+curr
        print(res)
        k-=1
    
    return res


s="abcd"
res=[]
for i in range(1,len(s)+1):
    res.append(largestSubstring(s,i))
print(res)
def solution(nums1,nums2):
    t = len(nums1)
    res=[]
    for i in range(t):
        temp = 0
        for j in range(t):
            print((j+t-i)%t,j)
            temp = temp+abs(nums1[(j+t-i)%t]-nums2[j])
        res.append(temp)
        print("temp",temp)
    print(res)

nums1 = [1,4,2,11]
nums2 = [10,1,8,4]
solution(nums1,nums2)
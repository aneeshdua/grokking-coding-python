def getFlaskType(requirements,markings,n,flaskTypes):
    properMarkings = [[] for i in range(flaskTypes)]
    for marking in markings:
        properMarkings[marking[0]].append(marking[1])
    print(properMarkings)
    globalWaste = float('inf')
    globalIdx = -1
    for i in range(flaskTypes):
        minimumMarkIdx=0
        flaskWaste = 0
        exceptionFlag=False
        for req in requirements:
            while(minimumMarkIdx < len(properMarkings[i]) and properMarkings[i][minimumMarkIdx]<req):
                minimumMarkIdx+= 1
            if minimumMarkIdx==len(properMarkings):
                exceptionFlag=True
                break
            else:
                flaskWaste += properMarkings[i][minimumMarkIdx]-req
        print("Flasktype",i,"\t","flaskWaste",flaskWaste,"\t")
        if not exceptionFlag and flaskWaste<globalWaste:
            globalWaste = flaskWaste
            globalIdx = i

    return globalIdx

# n=4
# requirements= [4,6,6,7]
# markings=[
#     [0, 3], [0, 5],[0, 7],
#     [1, 6], [1, 8],[1, 9],
#     [2, 3],[2, 5], [2, 6]
# ]
# flaskTypes = 3


n=2
requirements= [4,6]
markings=[
    [0, 5], [0, 7],[0,10],
    [1, 4], [1, 10],
]
flaskTypes = 2


# n=2
# requirements= [10,15]
# markings=[
#     [0, 11], [0, 20],
#     [1, 11], [1, 17],
#     [2, 12],[2, 16],
# ]
# flaskTypes = 3



ans = getFlaskType(requirements,markings,n,flaskTypes)
print(ans)
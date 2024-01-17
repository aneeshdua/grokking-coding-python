# https://leetcode.com/problems/first-missing-positive/description/
def firstKMissingPositive(self, nums: List[int], k: int) -> int:
    i,n = 0, len(nums)
    while i < n:
        j = nums[i]-1
        if nums[i] >0 and nums[i]<n and nums[i] != nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
        else:
            i+=1
    
    missing = []
    extra = set()
    for i in range(n):
        if len(missing) < k :
            if nums[i] != i+1:
                missing.append(i+1)
                extra.add(nums[i])

    i=1
    while len(missing) < k:
        candidate = i+n
        if candidate not in extra:
            missing.append(candidate)
        i+=1
    return missing


print(firstKMissingPositive([3, -1, 4, 5, 5], 3))
print(firstKMissingPositive([2, 3, 4], 3))
print(firstKMissingPositive([-2, -3, 4], 2))
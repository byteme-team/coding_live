#O(n2)
def TwoSum(nums,t):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == t:
                return [i,j]
    return [-1,-1]
    
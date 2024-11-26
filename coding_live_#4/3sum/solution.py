def threeSum(nums):
    out = set()
    nums = sorted(nums)
    
    for index, item in enumerate(nums):
        p1 = index + 1 
        p2 = len(nums)-1
        while p1 < p2:
            currentSum = item + nums[p1] + nums[p2]
            if currentSum == 0:
                out.add((item,nums[p1],nums[p2]))
                p2 -= 1
                p1 += 1
            elif currentSum > 0:
                p2 -= 1
            else:
                p1 += 1
        
    return [list(triplet) for triplet in out]


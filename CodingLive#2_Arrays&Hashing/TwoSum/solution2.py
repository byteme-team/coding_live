# O(nlog(n))
def twoSum(nums, target):
    nums = [(v, i) for i, v in enumerate(nums)]
    nums = sorted(nums)
    p1 = 0
    p2 = len(nums) - 1
    while (p1 < p2):
        sum_ = nums[p1][0] + nums[p2][0]
        if sum_ == target:
            return [nums[p1][1], nums[p2][1]]
        if sum_ > target:
            p2 -= 1
        else:
            p1 += 1
    return [-1, -1]

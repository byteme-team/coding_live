# O(n)
def twoSum(nums, target):
    hm = dict()
    for i, n in enumerate(nums):
        tmp = target - n
        if tmp in hm:
            return [hm[tmp], i]
        else:
            hm[n] = i
    return [-1, -1]

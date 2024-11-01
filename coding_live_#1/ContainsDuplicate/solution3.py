#O(n)
def containsDuplicate(nums):
    hash = dict()
    for n in nums:
        if n in hash:
            hash[n] += 1
        else: 
            hash[n] = 0
    for (k, v) in hash.items():
        if v > 0:
            return True
    return False

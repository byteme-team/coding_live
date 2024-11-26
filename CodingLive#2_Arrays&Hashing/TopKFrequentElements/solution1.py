# O(nlog(n))
def topKFrequent(nums, k):
    hm = dict()
    for n in nums:
        hm[n] = hm.get(n, 0) + 1
    out = []
    lst = sorted(hm.items(), key=lambda x: x[1], reverse=True)
    for key, val in lst[:k]:
        out.append(key)
    return out

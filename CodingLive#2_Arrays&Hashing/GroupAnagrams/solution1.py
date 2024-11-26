# O(nlog(n))
def groupAnagrams(strs):
    hm = dict()
    for s in strs:
        k = "".join(sorted(s))
        if k in hm:
            hm[k].append(s)
        else:
            hm[k] = [s]
    out = []
    for k, v in hm.items():
        out.append(v)
    return out

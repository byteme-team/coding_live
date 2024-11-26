#O(n)
def isAnagram(s, t):
    hash = dict()
    for c in s:
        if c in hash:
            hash[c]+=1
        else:
            hash[c]=1
    for c in t:
        if c in hash:
            hash[c]-=1
        else:
            hash[c]=-1
    for (k, v) in hash.items():
        if v != 0:
            return False
    return True

#O(n log(n))
def isAnagram(s, t):
    return sorted(s) == sorted(t)

    
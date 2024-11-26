def maxArea(height):
    _max = 0
    p1 = 0
    p2 = len(height) - 1
    while (p1 < p2):
        h = min(height[p1], height[p2])
        w = p2 - p1
        res = h * w
        if res > _max:
            _max = res
        if height[p1] < height[p2]:
            p1 += 1
        else:
            p2 -= 1
    return _max

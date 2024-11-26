def twoSum(numbers,target):
    p1 = 0
    p2 = len(numbers) - 1
    while(p1 < p2):
        res = numbers[p1] + numbers[p2]
        if res == target:
            return [p1+1,p2+1]
        
        if res > target:
            p2-=1
        else:
            p1+=1
    return [-1,-1]
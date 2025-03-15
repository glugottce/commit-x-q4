def min_distance(stalls, n, cows):
    stalls.sort()
    
    def place(min_dist):
        c = 1
        lp = stalls[0]
        for i in range(1, n):
            if stalls[i] - lp >= min_dist:
                c += 1
                lp = stalls[i]
                if c == cows:
                    return True
        return False
    
    l, r = 1, stalls[n-1] - stalls[0]
    re = 0
    
    while l <= r:
        mid = (l + r) // 2
        if place(mid):
            re = mid
            l = mid + 1
        else:
            r = mid - 1
    return re

n = int(input().strip())
stalls = list(map(int, input().strip().split()))
k = int(input().strip())
print(min_distance(stalls, n, k))
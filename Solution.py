def can_place(stalls, cows, min_gap):
    count = 1
    last_stall = stalls[0]
    
    for stall in stalls[1:]:
        if stall - last_stall >= min_gap:
            count += 1
            last_stall = stall
            if count == cows:
                return True
    return False

def max_min_distance(stalls, cows):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    best_gap = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place(stalls, cows, mid):
            best_gap = mid
            low = mid + 1
        else:
            high = mid - 1
    return best_gap

n = int(input())
stalls = list(map(int, input().split()))
cows = int(input())

print(max_min_distance(stalls, cows))
 

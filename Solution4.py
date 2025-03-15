def is_possible(arr, n, k, min_dist):
    cows_placed = 1  
    last_position = arr[0]

    for i in range(1, n):
        if arr[i] - last_position >= min_dist:
            cows_placed += 1
            last_position = arr[i]
            if cows_placed == k:
                return True

    return False

def max_min_distance(arr, n, k):
    arr.sort()  
    low, high = 1, arr[-1] - arr[0]  
    best = 0

    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, n, k, mid):
            best = mid  
            low = mid + 1  
        else:
            high = mid - 1

    return best

n = int(input())  
arr = list(map(int, input().split()))  
k = int(input())  

print(max_min_distance(arr, n, k))

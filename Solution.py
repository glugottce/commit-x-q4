def is_feasible(arr, n, k, dist):
    count, last_position = 1, arr[0]
    for i in range(1, n):
        if arr[i] - last_position >= dist:
            count += 1
            last_position = arr[i]
            if count == k:
                return True
    return False

def max_min_distance(arr, n, k):
    arr.sort()
    low, high = 1, arr[-1] - arr[0]
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(arr, n, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(max_min_distance(arr, n, k))

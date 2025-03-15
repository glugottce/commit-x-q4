def canPlace(arr, n, k, mid):
    cows = 1  
    last_pos = arr[0]  

    for i in range(1, n):
        if arr[i] - last_pos >= mid:
            cows += 1
            last_pos = arr[i]  
            if cows == k:
                return True  
    return False  

def maxDist(arr, n, k):
    arr.sort()  
    l, h = 1, arr[-1] - arr[0]  
    res = 0

    while l <= h:
        mid = (l + h) // 2  
        if canPlace(arr, n, k, mid):
            res = mid  
            l = mid + 1  
        else:
            h = mid - 1  
    
    return res

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(maxDist(arr, n, k))  

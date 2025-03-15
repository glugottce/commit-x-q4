n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()

low = 1
high = arr[-1] - arr[0]
res = 0

while low <= high:
    mid = (low+high)//2
    cows=1
    last = arr[0]
    for i in range(1,n):
        if arr[i] - last >= mid:
            cows+=1
            last = arr[i]
            if cows == k:
                res = mid
                low = mid+1
                break
    else:
        high = mid - 1
print(res)
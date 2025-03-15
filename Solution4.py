from itertools import combinations
n=int(input());arr=[int(i) for i in input().strip().split()];k=int(input())
lst=list(combinations(arr,k));mn=None
for i in lst:
    m=None
    for j in range(1,len(i)):
        x=abs(i[j]-i[j-1])
        if m is None or x<m:
            m=x
    if mn is None or m>mn:
        mn=m
print(mn)

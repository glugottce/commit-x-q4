n=int(input())
a=list(map(int,input().split()))
k=int(input())
#print(*a)
r=a[n-1]-a[0]
#print(r)
flag=0
new_flag=0
for i in range(1,r+1):
    count=1
    pos=a[0]
    for j in range(1,n):
        if a[j]-pos>=i:
            count+=1
            pos=a[j]
        if count==k:
            flag=1
            new_flag=i
            
if flag:
    print(new_flag)
else:
    print(-1)

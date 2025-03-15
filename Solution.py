n = int(input())
l = list(map(int, input().split()))
k = int(input())

l.sort()

cows = k
min_dist = l[1]-l[0]
pos_cows = [0]

for i in range(len(l)):
    if cows >= 0:
        dist = l[i+1]-l[i]
        if dist > min_dist:
            pos_cows.append(l[i])
        cows -= 1
    else:
        break

pos_cows.remove(0)

for i in range(len(pos_cows)-1):
    diff = l[i+1]-l[i]
    if diff > min_dist:
        min_dist = diff
print(min_dist, pos_cows)

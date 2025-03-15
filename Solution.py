def max_min_dist(a, k):
    a.sort()
    l, r, res = 1, a[-1] - a[0], 0

    def can_place(d):
        cnt, last = 1, a[0]
        for x in a[1:]:
            if x - last >= d:
                cnt += 1
                last = x
                if cnt == k:
                    return True
        return False

    while l <= r:
        m = (l + r) // 2
        if can_place(m):
            res, l = m, m + 1
        else:
            r = m - 1

    print(res)

n = int(input())
a = list(map(int, input().split()))
k = int(input())
max_min_dist(a, k)

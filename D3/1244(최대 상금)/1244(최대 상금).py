def dfs(num, idx, snum, sw):
    if snum == sw or idx == len(num) - 1:
        return snum
    if num[idx] == max(num[idx:]):
        dfs(num, idx + 1, snum, sw)
    else:
        midx = len(num) - 1
        for i in range(len(num) -1, idx, -1):
            if num[midx] < num[i]:
                midx = i
        num[idx], num[midx] = num[midx], num[idx]
        dfs(num, idx + 1, snum + 1, sw)


N = int(input())
for i in range(1, N + 1):
    num, sw = map(int, input().split())
    num = list(str(num))
    snum = dfs(num, 0, 0, sw)
    print(num,snum)
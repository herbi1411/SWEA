T = 10
N = 100
for t in range(1, T + 1):
    input()
    arr = [input() for _ in range(N)]
    dp1 = [[[False] * N for _ in range(N)] for __ in range(N)]
    dp2 = [[[False] * N for _ in range(N)] for __ in range(N)]
    maxK = 1
    for k in range(1):
        for i in range(N):
            for j in range(N):
                dp1[k][i][j] = True
                dp2[k][i][j] = True


    for k in range(1, N):
        for i in range(N):
            for j in range(N):
                if i + k < N and dp1[k - 2][i + 1][j] == True and arr[i][j] == arr[i + k][j]:
                    maxK = k
                    dp1[k][i][j] = True
                if j + k < N and dp2[k - 2][i][j + 1] == True and arr[i][j] == arr[i][j + k]:
                    maxK = k
                    dp2[k][i][j] = True

    print(maxK + 1)
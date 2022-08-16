T = 10
N = 2
for t in range(1, T + 1):
    input()
    arr = [input() for _ in range(N)]
    dp1 = [[[False] * N for _ in range(N)] for __ in range(N + 1)]
    dp2 = [[[False] * N for _ in range(N)] for __ in range(N + 1)]
    maxK = 1
    for k in range(2):
        for i in range(N):
            for j in range(N):
                dp1[k][i][j] = True
                dp2[k][i][j] = True


    for k in range(2, N + 1):
        for i in range(N):
            for j in range(N):
                if i + k - 1 < N and dp1[k - 2][i + 1][j] == True and arr[i][j] == arr[i + k - 1][j]:
                    maxK = k
                    dp1[k][i][j] = True
                if j + k - 1 < N and dp2[k - 2][i][j + 1] == True and arr[i][j] == arr[i][j + k - 1]:
                    maxK = k
                    dp2[k][i][j] = True

    print(f"#{t} {maxK}")
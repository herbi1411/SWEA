N = int(input())
for k in range(1, N + 1):
    M = int(input())
    arr = [list(map(int, list(input()))) for _ in range(M)]
    answer = 0
    for i in range(M):
        for j in range(abs(M // 2 - i), M - abs(M // 2 - i)):
            answer += arr[i][j]
    print("#", k, " ", answer, sep='')
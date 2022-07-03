T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    ans = -2147483648  # input 배열 값의 범위가 안정해져있음
    if N > M:
        N, M = M, N
        arr1, arr2 = arr2, arr1
    for j in range(M - N + 1):
        temp = 0
        for k in range(N):
            temp += arr1[k] * arr2[j + k]
        ans = max(ans, temp)
    print("#{0} {1}".format(i + 1, ans))
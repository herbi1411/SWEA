N = 10
for i in range(1, N + 1):
    M = int(input())
    arr = list(map(int, input().split()))
    for j in range(M):
        maxVal = max(arr)
        minVal = min(arr)
        minIdx = arr.index(minVal)
        maxIdx = arr.index(maxVal)
        arr[minIdx] += 1
        arr[maxIdx] -= 1
    answer = max(arr) - min(arr)
    print("#", i, " ", answer, sep='')
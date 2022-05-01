N = 10

for i in range(1, N + 1):
    M = int(input())
    answer = 0
    arr = list(map(int, input().split()))
    for j in range(2, M - 2):
        leftMax = max(arr[j - 1], arr[j - 2])
        rightMax = max(arr[j + 1], arr[j + 2])
        answer += max(arr[j] - max(leftMax, rightMax), 0)
    print("#", i, " ", answer, sep="")
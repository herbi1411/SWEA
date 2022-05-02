def pow(a, b):
    if b == 0:
        return 1
    return a * pow(a, b - 1)


N = 10
for _ in range(N):
    i = int(input())
    a, b = map(int, input().split())
    print("#", i, " ", pow(a, b), sep='')
N = int(input())
for num in range(1, N + 1):
    temp = num
    cnum = 0
    while temp > 0:
        if temp % 10 in [3, 6, 9]:
            cnum += 1
        temp //= 10
    if cnum > 0:
        print("-" * cnum, end=" ")
    else:
        print(num, end=" ")
T = int(input())

for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    cdict = {}

    for c in str1:
        if c not in cdict:
            cdict[c] = 0

    for c in str2:
        if c in cdict:
            cdict[c] += 1

    ans = cdict[max(cdict, key=lambda x: cdict[x])]
    print(f"#{t} {ans}")
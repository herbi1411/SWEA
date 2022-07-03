N = 10
for _ in range(N):
    i = input()
    target = input()
    s = list(input())
    answer = 0
    for k in range(len(s) - len(target) + 1):
        if ''.join(s[k:k + len(target)]) == target:
            answer += 1
    print("#", i, " ", answer, sep='')
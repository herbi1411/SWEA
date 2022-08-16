def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    flag = False
    ans = ""
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if flag:
                break
            for k in range(N - M + 1 - j):
                if isPalindrome(arr[i][j + k:j + k + M]):
                    flag = True
                    ans = arr[i][j + k:j + k + M]
                    break
            for k in range(N - M + 1 - i):
                if isPalindrome(''.join([arr[i + v + k][j] for v in range(M)])):
                    flag = True
                    ans = ''.join([arr[i + v + k][j] for v in range(M)])
                    break
    print(f"#{t} {ans}")

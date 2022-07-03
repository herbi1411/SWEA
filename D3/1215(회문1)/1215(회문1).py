def isPalindrome(lst):
    for v in range(l // 2):
        if lst[v] == lst[len(lst) - v - 1]:
            continue
        else:
            return False
    return True


N = 10
for k in range(1, N + 1):
    l = int(input())
    arr = [list(input()) for _ in range(8)]
    answer = 0
    for i in range(8):
        for j in range(8):
            lst = []
            for m in range(l):
                if i + m >= 8:
                    break
                lst.append(arr[i + m][j])
            if len(lst) == l:
                isPal = isPalindrome(lst)
                if isPal:
                    answer += 1

            lst = []
            for m in range(l):
                if j + m >= 8:
                    break
                lst.append(arr[i][j + m])
            if len(lst) == l:
                isPal = isPalindrome(lst)
                if isPal:
                    answer += 1
    print("#", k, " ", answer, sep='')

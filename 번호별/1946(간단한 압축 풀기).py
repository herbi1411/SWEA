T = int(input())
for i in range(T):
    N = int(input())
    s = ""
    temp = 0
    for j in range(N):
        C, K = input().split()
        s += C * int(K)
    print("#{0}".format(i + 1))
    while temp + 10 < len(s):
        print(s[temp:temp + 10])
        temp += 10
    print(s[temp:])
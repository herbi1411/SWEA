T = int(input())

for t in range(1, T + 1):
    A, B = input().split()
    cnt = A.count(B)
    print(f"#{t} {len(A) - len(B) * cnt + cnt}")
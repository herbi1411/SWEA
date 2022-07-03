A, B = map(int, input().split())
if A - (B % 3) == 1:  # (1, 3), (2, 1), (3, 2)
    print('A')
else:
    print('B')
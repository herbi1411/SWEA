N = int(input())
for k in range(1, N + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    rowArr = arr
    colArr = [[arr[i][j] for i in range(9)] for j in range(9)]
    sqrArr = [[arr[i % 3 * 3 + j // 3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)]
    answer = 1
    for row, col, sqr in zip(rowArr, colArr, sqrArr):
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9:
            continue
        else:
            answer = 0
            break
    print("#", k, " ", answer, sep="")
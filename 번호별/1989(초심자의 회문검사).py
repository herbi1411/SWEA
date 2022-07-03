N = int(input())
for i in range(N):
    text = input()
    len_text = len(text)
    flag = True
    for j in range(len_text // 2):
        if text[j] != text[len_text - j - 1]:
            flag = False
            break
    print('#', i + 1, sep="", end=" ")
    if flag:
        print(1)
    else:
        print(0)
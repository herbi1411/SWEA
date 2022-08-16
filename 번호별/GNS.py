nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
numDict = {}
for i, num in enumerate(nums):
    numDict[num] = i

def compare(a):
    return numDict[a]

T = int(input())
for t in range(1, T + 1):
    input()
    lst = input().split()
    lst.sort(key = compare)
    print(f"#{t}")
    print(*lst)
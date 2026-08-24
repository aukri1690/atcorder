# (方針) N個 - 1番多い色 = 操作の回数

from collections import Counter

N = int(input())
C = list(map(int, input().split()))
C = Counter(C)

print(N - C.most_common()[0][1])
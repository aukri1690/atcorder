N = int(input())
L = list(map(int, input().split()))

total = sum(L)
left = 0
answer = float("inf")

for i in range(N-1):
  left += L[i]
  right = total - left
  answer = min(answer, abs(left - right))

print(answer)

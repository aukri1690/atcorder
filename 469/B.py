N = int(input())
S = list(input())

count = 0

# 番兵
S.insert(0, "x")
S.append("x")

print(S)

for i in range(1, N+1):
  if (S[i-1] == S[i] == S[i+1] == "x"):
    count += 1

print(count)

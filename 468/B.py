M, D = map(int, input().split())
S = list(input())

count = 0

for i in range(len(S)):
  if S[i] == "G":
    count += 1

  if S[i] == ".":
    for j in range(max(0, i-D), min(len(S), i+D+1)):
      if S[j] == "G":
        count += 1
        break

print(M - count)
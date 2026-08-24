S = list(input())

for i in range(len(S)):
  if S[i] != "A":
    S[i] = "."

result = "".join(S)

print(result)

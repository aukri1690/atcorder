N = int(input())
H, L = zip(*(map(int, input().split()) for _ in range(N)))
Q = int(input())
T = list(map(int, input().split()))

for i in range(len(T)):
  max_height = []
  for j in range(len(L)):
    if (T[i] + 0.5) < L[j]:
      max_height.append(H[j])
  print(max(max_height))
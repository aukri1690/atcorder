N, M, K = map(int, input().split())
A = list(map(int, input().split()))

calorie =[]

for i in range(N):
    #その日に食べるおやつのカロリーをリストに追加
    calorie.append(A[i])

    #カロリーのリストがM個を超えたら、古い日のカロリーを削除
    if len(calorie) > M:
        calorie.pop(0)

    #カロリーの合計がK以下であればYes
    if sum(calorie) <= K:
        print("Yes")

    #Noであればその日のカロリーは0として計上する
    else:
        print("No")
        calorie.pop(-1)
        calorie.append(0)

# k번째 큰 수


N, K = map(int, input().split())
N_list = list(map(int, input().split()))

res = set()

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1,N):
      res.add(N_list[i] + N_list[j] + N_list[k])


res = list(res)
res.sort(reverse=True)
print(res[K-1])
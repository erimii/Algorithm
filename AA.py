#k 번째 수

# T
# N s e k -> N개의 수 에서 s번째 ~ e번째 중 k 번째로 작은 수 출력
# N개의 수 작성

T = int(input())
result = []

for t in range(T):
  N, s, e, k = map(int, input().split())
  N_list = list(map(int, input().split()))
  N_list = N_list[s-1:e]
  N_list.sort()
  print("#{} {}".format(t+1, N_list[k-1]))
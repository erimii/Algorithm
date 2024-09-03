# 정다면체
# 정 N면체, 정 M면체 주사위를 던져서 나올 수 있는 눈의 합 중 확률이 가장 높은 것 구하기
# 답이 여러개인 경우 오름차순으로 출력

n, m = map(int, input().split())
sum_list = [0]*(n+m+1)

for i in range(1,n+1):
  for j in range(1,m+1):
    sum_list[i+j] += 1
    
for idx, x in enumerate(sum_list):
  if x == max(sum_list):
    print(idx, end=' ')
# 대표값
# N명의 학생의 성적 평균 구한 후, 그 값과 가작 가까운 성적의 학생 번호 찾기
# 답이 2개일 경우 성적 높은 학생으로
# 점수 여러개일 경우 제일 빠른 번호로

N = int(input())
s_list = list(map(int, input().split()))

avg = round(sum(s_list) / N)
dff = abs(avg - s_list[0])
score = 0

for idx, x in enumerate(s_list):
  if dff > abs(avg-x):
    dff = abs(avg-x)
    score = x
    res = idx+1
  elif dff == abs(avg-x):
    if score < x:
      res = idx+1

print(avg, res)
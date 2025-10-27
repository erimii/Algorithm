# bj_1193 분수 찾기

# 1. X가 몇 번째 대각선 안에 있는지 구하기. ~1, ~3, ~6, ~10..
# 2. X가 해당 대각선의 몇 번째에 있는지 구하기 1~, 2~, 4~, 7~.. 
# 3. 대각선 번호가 홀수면 위로 올라가는 방향, 짝수면 아래로 내려가는 방향.

x = int(input())
line=1

while x> line:
  x -= line
  line += 1

if line%2 == 0:
  # 분모가줄어듬
  m = line-x+1
  c = x
else:
  m = x
  c = line-x+1

print(f"{c}/{m}")
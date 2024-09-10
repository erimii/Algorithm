# 두 리스트 합치기

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

# lst = n_lst + m_lst
# lst.sort()

lst = []
p1 = p2 = 0

while p1<N and p2 <M:
  if n_lst[p1] <= m_lst[p2]:
    lst.append(n_lst[p1])
    p1 += 1
  else:
    lst.append(m_lst[p2])
    p2 +=1

if p1 < N:
  lst = lst + n_lst[p1:]
if p2 < M:
  lst = lst + m_lst[p2:]

for x in lst:
  print(x, end = ' ')
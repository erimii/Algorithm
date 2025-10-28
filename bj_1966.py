# bj_1966 프린터 큐

# 맨앞에꺼 빼서 뒤에꺼랑 우선순위 비교
# 우선순위가 더 큰게 있으면 맨 뒤로 다시 넣기
# 없으면 cnt+=1 하고 다시 첨부터 반복

import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  prior = list(map(int, input().split()))
  dq = deque([(i,p) for i, p in enumerate(prior)])
  cnt = 0

  while dq:
    idx, importance = dq.popleft()
    if any(importance < q[1] for q in dq):
      dq.append((idx, importance))
    else:
      cnt+=1
      if idx == m:
        print(cnt)
        break
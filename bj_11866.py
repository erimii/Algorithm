# bj_11866 요세푸스 문제 0

import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))
result=[]

while queue:
  queue.rotate(-(k-1))
  result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")
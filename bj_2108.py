# bj_2108 통계학

import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

mean = round(sum(nums)/n)
median = nums[n//2]
print(mean)
print(median)

cnt = Counter(nums).most_common()
max_freq = cnt[0][1]
modes = [num for num, freq in cnt if freq == max_freq]
if len(modes) == 1:
  print(modes[0])
else:
  print(sorted(modes)[1])

rng = nums[-1]-nums[0]
print(rng)


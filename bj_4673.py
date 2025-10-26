# bj_4673

def d(n):
  return n + sum(map(int, str(n)))

numbers = set(range(1,10001))
dn = set()

for i in range(1, 10001):
  dn.add(d(i))

self_nums = sorted(numbers - dn)

for num in self_nums:
  print(num)
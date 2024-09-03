# 자릿수의 합
# N개의 자연수, 각 자릿수의 합이 가장 큰 자연수 출력

# def digit_sum(x):
#   sum = 0
#   while x > 0:
#     sum += x%10
#     x //= 10
#   return sum

def digit_sum(x):
  sum = 0
  for i in str(x):
    sum += int(i)
  return sum

N = int(input())
n_list = list(map(int, input().split()))
max = 0

for x in n_list:
  if max < digit_sum(x):
    max = digit_sum(x)
    res = x

print(res)
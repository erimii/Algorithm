# 백준 1316 그룹 단어 체커

# 현재 문자와 다음 문자가 다르면 -> 현재 문자가 뒤에 또 나오는지 확인 -> 나오면 그룹단어 아님

n = int(input())
result = 0

for _ in range(n):
  word = input().strip()
  for i in range(len(word)-1):
    if word[i] != word[i+1] and word[i] in word[i+1:]:
      break
  else:
      result +=1


print(result)
# bj_17413 단어 뒤집기 2

s = input().rstrip()

result = ''
stack = ''
flag = False

for ch in s:
  if ch == '<':
    result += stack[::-1]
    flag=True
    stack=''
    result +=ch
  elif ch == '>':
    flag=False
    result +=ch
  elif flag:
    result += ch
  else:
    if ch == ' ':
      result += stack[::-1]+ ' '
      stack=''
    else:
      stack +=ch

result +=stack[::-1]

print(result)
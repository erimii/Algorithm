# bj_2941 크로아티아 알파벳

word = input().strip()

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for w in croa:
  word = word.replace(w, '*')

print(len(word))
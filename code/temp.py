user = input("")
for i in user:
  s = []
  s.append(i)
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(abc)):
  for j in range(len(s)):
    if abc[i] == s[j]:
      abc[i] = j
      break
    else:
      abc[i] = -1
      
for i in abc:
  print(i, " ")

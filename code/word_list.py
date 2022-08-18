s = input().lower()
word_list = list(set(s))
cnt = []
for i in word_list:
  count = s.count(i)
  cnt.append(count)
if cnt.count(max(cnt)) >= 2:
  print("?")
else:
  print(word_list[(cnt.index(max(cnt)))].upper())
  

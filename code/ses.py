num = int(input())
count =0
for i in range(num):
  S = input()
  temp = []
  for j in S:
   
    temp.append(j)
  for j in range(len(temp)):
    if S.count(temp[j]) >= 2:
      if j == 0:
        if temp[j] != temp[j+1]:
          break
      elif j == len(temp)-1:
        if temp[j] != temp[j-1]:
          break
      else:
        if temp[j] != temp[j-1] and temp[j] != temp[j+1]:
          break
      
    if j == len(temp)-1:
      count= count+1
print(count)

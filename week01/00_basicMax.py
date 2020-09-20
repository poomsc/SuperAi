n = int(input("How many number do you have? : "))
max = 0
for i in range(n):
  tmp = int(input())
  if i==0:
    max = tmp
    continue
  max = max if max > tmp else tmp
print(max)
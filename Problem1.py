import time

n=0
for i in range(1,1000):
  if i % 3 == 0:
    n += i
  elif i % 5 == 0:
    n += i
  else:
    print("")
  print(n)

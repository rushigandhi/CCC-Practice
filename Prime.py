num = int(input())
i = 0
while (i < num):
  if (i == 2):
    print(i)
  if (i == 3):
    print(i)
  if (i % 2):
    i += 1
  if (i % 3):
    i += 1
  n = 5
  w = 2
  while (n * n <= i):
    if (i % n == 0):
      i += 1
    i += w
    w = 6 - w
    print(i)
  

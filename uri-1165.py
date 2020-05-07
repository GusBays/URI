N = int(input())
i = 0

while i < N:
  num = int(input())
  i = i + 1
  x = 0
  y = 1
  while y<= num:
      if num % y == 0:
         x = x + 1
      y = y + 1
  if x > 2:
      print('%d nao eh primo' % (num))
  else:
    print('%d eh primo' % (num))
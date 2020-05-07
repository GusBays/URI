def pontos():
  D = int(input())
  if D <= 800:
    print(1)
  else:
    if D > 800 and D <= 1400:
      print(2)
  if D > 1400 and D <= 2000:
    print(3)


pontos()
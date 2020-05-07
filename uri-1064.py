pos = 0
i = 1
cont = 0
soma = 0

while i <= 6:
  num = float(input())

  if num > 0:
    pos = pos + 1
    cont += 1
    soma += num

  i = i + 1

  media = soma/cont

print('%d valores positivos' % (pos))
print('%.1f' % (media))
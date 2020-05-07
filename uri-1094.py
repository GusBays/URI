N = int(input())
i = 0
c = 0
r = 0
s = 0
pc = 0
pr = 0
ps = 0

while i < N:
  x = input().split()
  a,b = x
  if b == 'C':
    c = c + int(a)
  elif b == 'R':
    r = r + int(a)
  elif b == 'S':
    s = s + int(a)
  total = 0
  total = total + c + r + s
  pc = (c/total) * 100
  pr = (r/total) * 100
  ps = (s/total) * 100
  i = i + 1

print('Total: %d cobaias' % (total))
print('Total de coelhos: %d' % (c))
print('Total de ratos: %d' % (r))
print('Total de sapos: %d' % (s))
print('Percentual de coelhos: %.2f' % (pc) + ' %')
print('Percentual de ratos: %.2f' % (pr) + ' %')
print('Percentual de sapos: %.2f' % (ps) + ' %')
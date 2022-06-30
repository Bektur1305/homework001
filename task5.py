def get_prime_factors(n):
    factors = list()
    divisor = 2
    while divisor <= n:
        if n%divisor==0:
            factors.append(divisor)
            n = n/divisor
        else:
            divisor+=1
    return factors
def count_find_num():
  print('primesL = ', end=' ')
  qc= input().split()
  ss=[]
  for k in range(len(qc)):
    ss.append(int(qc[k]))
  ss=set(ss)
  print('limit = ', end=' ')
  a = int(input())
  dd = {}
  for i in range(2, a+1):
      c = get_prime_factors(i)
      c = set(c)
      dd.update({i: c})
  c = 0
  dd2 = {}
  max = 0
  for j in range(2, a+1):
      if ss == dd.get(j):
        dd2.update({j: dd.get(j)})
        max = j
        c += 1
  return c, max
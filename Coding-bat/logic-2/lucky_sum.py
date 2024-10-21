def lucky_sum(a, b, c):
  return 0 if a==13 else a if b==13 else a+b if c==13 else a+b+c

lucky_sum(1, 2, 3)
lucky_sum(1, 2, 13)
lucky_sum(1, 13, 3)
def in1to10(n, outside_mode):
  if outside_mode:
    return True if n <= 1 or n >= 10 else False
  else:
    return True if 1<=n<=10 else False

in1to10(5, False)
in1to10(11, False)
in1to10(11, True)
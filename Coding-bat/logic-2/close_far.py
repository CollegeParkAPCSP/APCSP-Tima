def close_far(a, b, c):
  if abs(b-a) <= 1:
    return True if ((abs(c-a) >= 2) and (abs(c-b) >= 2)) else False
  return True if ((abs(b-a) >= 2) and (abs(b-c) >= 2)) else False

close_far(1, 2, 10)
close_far(1, 2, 3)
close_far(4, 1, 3)
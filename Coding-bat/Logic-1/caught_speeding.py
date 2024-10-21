def caught_speeding(speed, is_birthday):
  if is_birthday:
    return 0 if speed<=65 else 1 if speed <= 85 else 2
  else:
    return 0 if speed<=60 else 1 if speed <= 80 else 2

caught_speeding(60, False)
caught_speeding(65, False)
caught_speeding(65, True)
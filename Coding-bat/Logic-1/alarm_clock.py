def alarm_clock(day, vacation):
  wday = 1 <= day <= 5
  if vacation:
    return '10:00' if wday else 'off'
  else:
    return '7:00' if wday else '10:00'

alarm_clock(1, False)
alarm_clock(5, False)
alarm_clock(0, False)
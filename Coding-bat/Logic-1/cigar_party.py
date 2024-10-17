def cigar_party(cigars, is_weekend):
  if is_weekend:
    return True if cigars >= 40 else False
  else:
    return True if 40 <= cigars <= 60 else False

cigar_party(30, False)
cigar_party(50, False)
cigar_party(70, True)
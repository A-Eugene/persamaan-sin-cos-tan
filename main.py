def cariDHP(A, formula, memenuhiBatasan):
  DHP = []
  absoluteK = 0

  Naik = True
  sudahMenemukanDariNaik = False

  Turun  = True
  sudahMenemukanDariTurun = False

  while Naik and Turun:
    x = formula(A, absoluteK)

    if Naik:
      if memenuhiBatasan(x):
        DHP.append(x)
        sudahMenemukanDariNaik = True
      else:
        if sudahMenemukanDariNaik:
          Naik = False

    if Turun:
      if memenuhiBatasan(x):
        DHP.append(x)
        sudahMenemukanDariTurun = True
      else:
        if sudahMenemukanDariTurun:
          Turun = False

    absoluteK += 1

  return list(dict.fromkeys(DHP))

def cariDHPSin(A, memenuhiBatasan):
  def formula1(A, K):
    return A + K * 360

  def formula2(A, K):
    return (180 - A) + K * 360

  payload = cariDHP(A, formula1, memenuhiBatasan) + cariDHP(A, formula2, memenuhiBatasan)
  payload.sort()

  return payload

def cariDHPCos(A, memenuhiBatasan):
  def formula1(A, K):
    return A + K * 360

  def formula2(A, K):
    return -A + K * 360

  payload = cariDHP(A, formula1, memenuhiBatasan) + cariDHP(A, formula2, memenuhiBatasan)
  payload.sort()

  return payload

def cariDHPTan(A, memenuhiBatasan):
  def formula(A, K):
    return A + K * 180

  payload = cariDHP(A, formula, memenuhiBatasan)
  payload.sort()

  return payload

# CONTOH INPUT

def batasan(x):
  return 0 <= x <= 360

print(cariDHPCos(63, batasan))

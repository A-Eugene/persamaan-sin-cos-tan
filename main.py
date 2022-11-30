def cariDHP(A, formula, memenuhiBatasan):
  DHP = []
  k = 0

  sudahPernahMenemukan = False

  while True:
    xTerpenuhi = False
    yTerpenuhi = False

    x = formula(A, k)
    y = formula(A, -k)

    if memenuhiBatasan(x):
      DHP.append(x)
      adaDariNaik = True
      sudahPernahMenemukan = True

    if memenuhiBatasan(y):
      DHP.append(y)
      yTerpenuhi = True
      sudahPernahMenemukan = True

    if sudahPernahMenemukan and adaDariNaik == False and yTerpenuhi == False:
      break
    else:
      k += 1
  
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

# INPUT

def batasan(x):
  return -10000 <= x <= 10000

print(cariDHPCos(63, batasan))

    
    

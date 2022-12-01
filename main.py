def cariDHP(A, formula, memenuhiBatasan):
  DHP = []
  k = 0

  sudahPernahMenemukan = False

  while True:
    xTerpenuhi = False
    yTerpenuhi = False

    x = formula(A, k)
    y = formula(A, -k)

# Jika k positif masuk dalam DHP, yaitu ketika xTerpenuhi dan yTerpenuhi = True 
# dan sudahPernahMenemukan = True

    if memenuhiBatasan(x):
      DHP.append(x)
      xTerpenuhi = True
      sudahPernahMenemukan = True

    if memenuhiBatasan(y):
      DHP.append(y)
      yTerpenuhi = True
      sudahPernahMenemukan = True

# Kalo belum pernah menyentuh DHP, dan k tidak masuk dalam DHP, break
# == beda dengan =, = berarti assign kanan ke kiri, == berarti sama dengan

    if sudahPernahMenemukan and xTerpenuhi == False and yTerpenuhi == False:
      break
    else:
      k += 1
  
# Fungsi untuk menghilangkan duplikat

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
  return -360 <= x <= 360

print(cariDHPSin(60, batasan))
print(cariDHPCos(60, batasan))
print(cariDHPTan(60, batasan))

    
    

def cariDHP(A, formula, memenuhiBatasan):
  DHP = []
  k = 0 

# [] = list (daftar)
# k = 0 sebagai titik awal, nantinya bisa dijadikan positif maupun negatif

  sudahPernahMenemukan = False

  while True:
    xTerpenuhi = False
    yTerpenuhi = False

    x = formula(A, k)
    y = formula(A, -k)

    if memenuhiBatasan(x):
      DHP.append(x)
      xTerpenuhi = True
      sudahPernahMenemukan = True

    if memenuhiBatasan(y):
      DHP.append(y)
      yTerpenuhi = True
      sudahPernahMenemukan = True

# Kalau sudah tidak di dalam DHP, break
# == beda dengan =, = berarti assign kanan ke kiri, == berarti sama dengan 
    
  if sudahPernahMenemukan and xTerpenuhi == False and yTerpenuhi == False:
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

# CONTOH INPUT

# def batasan(x):
#   return 0 <= x <= 360

# print(cariDHPCos(60, batasan))

    
    

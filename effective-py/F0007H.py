# 3 lehetőség szám kitalálására
number = 5
hits = 0
result = False
print('Gondoltam egy számot 1-5 között! Kitalálod?')
while not result and hits != 3:
  A=int(input('Melyik lehet ez a szám?'))
  if hits == 0 and A != number:
    print('Nem talált! Csak ' , number-A, ' , amit tévedtél! Van még 2 lehetőséged!', sep='')
  elif hits < 2 and A != number:  
    print('Nem talált! Csak ' , number-A, ' , amit tévedtél! van még 1 lehetőséged!', sep='')
  elif hits <= 3 and A != number:
    print('Nem talált! Csak ' , number-A, ' , amit tévedtél! Nincs már lehetőséged! Sajnálom!',sep='')
  else:
    print('Gratulálok, eltaláltad!')
    result = True
  hits = hits  + 1

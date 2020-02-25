def numMayor(a,b,c):
  lista = []
  numeroMax = 0
  posicionMax = 0
  lista.append(a)
  lista.append(b)
  lista.append(c)
  numeroMax = max(lista)
  print("El número mayor es: " + str(numeroMax))
  posicionMax = lista.index(numeroMax) + 1
  print("Y la posición es: " + str(posicionMax))

numMayor(1,3,2)

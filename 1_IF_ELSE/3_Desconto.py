valorInicial = int(input("Insira o valor inicial: "))

if valorInicial >= 0 and valorInicial <= 50:
  valorDesconto = valorInicial*0.95
  print("Valor com desconto: " + str(valorDesconto))
elif valorInicial > 50 and valorInicial <= 100:
  valorDesconto = valorInicial*0.9
  print("Valor com desconto: " + str(valorDesconto))  
elif valorInicial > 100:
  valorDesconto = valorInicial*0.85
  print("Valor com desconto: " + str(valorDesconto))  
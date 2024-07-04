lado1 = int(input("Insira o primeiro lado: "))
lado2 = int(input("Insira o segundo lado: "))
lado3 = int(input("Insira o terceiro lado: "))

if lado1+lado2 < lado3 or lado1+lado3 < lado2 or lado2+lado3 < lado1:
  print("Os valores não formam um triângulo válido")
else:
  if lado1 == lado2 == lado3:
    print("O triângulo é equilátero. Todos os lados são iguais")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles. Possui dois lados iguais")
  else:
    print("O triângulo é escaleno. Todos os lados são diferentes")
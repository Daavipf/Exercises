idade = int(input("Digite sua idade: "))

if idade <= 12 and idade >= 0:
  print("Você é criança")
elif idade > 12 and idade <= 17:
  print("Você é adolescente")
elif idade > 17 and idade <= 64:
  print("Você é adulto")
elif idade > 64:
  print("Você é idoso")
else:
  print("Idade inválida")

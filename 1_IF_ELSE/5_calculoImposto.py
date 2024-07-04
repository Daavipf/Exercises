salario = float(input("Insira seu salário: "))

if salario <= 1903.98:
  print("Você está isento do imposto de renda")
else:
  if salario <= 2826.65:
    imposto = (salario-1903.98)*0.075
  elif salario <= 3751.05:
    imposto = (salario-2826.65)*0.15
  elif salario <= 4664.68:
    imposto = (salario-3751.05)*0.225
  else:
    imposto = (salario-4664.68)*0.275

  print(f"Seu imposto será de: R${imposto:.2f}")
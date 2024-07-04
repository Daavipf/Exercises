frase = input("Digite uma palavra ou frase: ")
frase_limpa = ""

for char in frase:
  if char.isalnum():
    frase_limpa += char.lower()

if frase_limpa == frase_limpa[::-1]:
  print("É um palíndromo")
else:
  print("Não é um palíndromo")
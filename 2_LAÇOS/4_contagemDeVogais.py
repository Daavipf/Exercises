import unicodedata

frase = input("Digite uma palavra ou frase: ")
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

frase_limpa = unicodedata.normalize('NFKD', frase).encode('ASCII', 'ignore').decode('ASCII')

for char in frase_limpa.lower():
  for vogal in vogais:
    if char == vogal:
      contador +=1 

print(contador)
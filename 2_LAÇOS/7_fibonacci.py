numero = int(input("DIgite um numero: "))

sequencia = [0,1]

for x in range(1, numero):
  atual = sequencia[x]
  antecessor = sequencia[x-1]
  sequencia.append(atual+antecessor)

print(sequencia)
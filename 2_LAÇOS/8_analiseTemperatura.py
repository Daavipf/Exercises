# Exercício 7: Filtragem de Dados de Temperatura
# Você trabalha em uma empresa de meteorologia que analisa dados de temperatura. Recebeu uma lista de temperaturas registradas ao longo de um mês e precisa identificar dias com 
# temperaturas anormais. Considere como temperatura anormal qualquer valor abaixo de -10°C ou acima de 35°C. Escreva um programa que percorra a lista de temperaturas e exiba uma 
# mensagem de alerta para cada temperatura anormal. Se encontrar três dias consecutivos com temperaturas anormais, o programa deve interromper a análise imediatamente.

temperaturas = [22, 25, 19, -12, 32, 40, 33, 28, 31, 30, 36, -15, 27, 25, 24, 29, 30, 26, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]
temperaturas_anormais = []
contador_temp_anormais = 0

for temp in temperaturas:
  if temp > 35 or temp < -10:
    temperaturas_anormais.append(temp)
    contador_temp_anormais += 1
    print("Alerta:", temperaturas_anormais[-1], "°C Dia:", temperaturas.index(temp))
  else:
    contador_temp_anormais = 0
  
  if contador_temp_anormais == 3:
    print("Período anormal detectado")
    break
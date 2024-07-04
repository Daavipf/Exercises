primos = [1, 2, 3, 5, 7]

for x in range(1, 101):
  if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 !=0 and x != 1:
    primos.append(x)

print(primos)
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)



#usando break no for range

for numero in range(100):
    
    if numero == 10:
        break

    print(numero)


#usando continue no for range
for numero in range(100):
    
    if numero == 10:
        continue

    print(numero, end=" ")


#usando continue com numeros impares apenas (removendo os pares)
for numero in range(100):
    
    if numero % 2 == 0:
        continue

    print(numero, end=" ")











num = int(input("Digite um número: "))

if num > 0:
    elevado = num**2
    print(f"O número {num} ao quadrado é {elevado}")
    raiz = (num ** (1/2))
    print(f"A raiz quadrada de {num} é {raiz}")
else:
    print("Encerrando...")
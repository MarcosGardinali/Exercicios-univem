op = int(input("Digite o valor de OP"))
base = float(input("Digite o valor da base"))
altura = float(input("Digite o valor da altura"))

print("A)")
if op == 1:
    area = base*altura
    print(f'Área = {area}')
else:
    print("Não foi possível calcular")

print("B)")
if op == 2:
    area = (base*altura)/2
    print(f'Área = {area}')
else:
    print("Não foi possível calcular")

kmPercorridos = int(input("Digite quantos Km foram percorridos: "))
quantDias = int(input("Digite a quantidade de dias de uso: "))

total = (kmPercorridos*0.15) + (quantDias*60)

print(f'O valor total gasto é de {total}')
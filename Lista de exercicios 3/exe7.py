distancia = int(input("Digite a distância percorrida: "))
gastoLitros = int(input("Digite a quantidade de combustível consumida: "))

consumo = distancia/gastoLitros

print(f"O consumo médio do veículo é {consumo:.2f} Km/L")
if consumo <= 8:
    print("Venda o carro!")
elif consumo > 8 and consumo <= 14:
    print("Econômico!")
else: 
    print("Super Econômico!")
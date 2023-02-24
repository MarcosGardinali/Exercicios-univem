precoLitro = int(input("Digite o preço do litro do combustível: "))
desempenho = int(input("Digite o desempenho do veículo: "))
distancia = int(input("Digite a distancia percorrida: "))

litrosGastos = distancia/desempenho
gasto = precoLitro*litrosGastos

print(f'O desempenho do veículo foi de {desempenho} Km/l')
print(f'O total gasto foi de R$ {gasto}')

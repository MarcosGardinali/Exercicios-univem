lado1 = int(input("Digite o primeiro lado do triângulo"))
lado2 = int(input("Digite o segundo lado do triângulo"))
lado3 = int(input("Digite o terceiro lado do triângulo"))

if lado1 == lado2 and lado2 == lado3:
    print("O triângulo é Equilátero")
elif lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado1 != lado2 or lado3 == lado2 and lado3 != lado1:
    print("O Triângulo é Isóceles")
else:
    print("O Triângulo é Escaleno")

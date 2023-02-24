angulo1 = int(input("Digite o primeiro ângulo: "))
angulo2 = int(input("Digite o segundo ângulo: "))
angulo3 = int(input("Digite o terceiro ângulo: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Triângulo Retângulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3> 90:
    print("Triângulo Obtusângulo")
elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("Triângulo Acutângulo")
else:
    print("Ecerrado...")

angTotal = angulo1 + angulo2 + angulo3

if angTotal == 180:
    print(f'O Triângulo tem um angulo de {angTotal}')
else:    
    print(f'A soma dos 3 angulos é = {angTotal}')
    
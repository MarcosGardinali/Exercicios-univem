num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 < num3:
    resultado = (f'{num2}{num1}{num3}')
    print(resultado)
elif num2 > num1 and num2 < num3:
    resultado = (f'{num1}{num2}{num3}')
    print(resultado)
elif num3 > num1 and num3 < num2:
    resultado = (f'{num1}{num3}{num2}')
    print(resultado)
else:
    resultado = (f'{num3}{num2}{num1}')    
    print(resultado)

    
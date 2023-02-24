salario = float(input("Digite seu salário: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

if prestacao >= (salario*0.2):
    print(f"Empréstimo não concecido")
else:
    print(f"Empréstimo concecido")
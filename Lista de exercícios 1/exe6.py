salAtual = int(input("Digite o valor do salário: "))
reajuste = int(input("Digite a porcentagem de reajuste: "))

reajuste = reajuste/100
salNovo = salAtual+(salAtual*reajuste)

print(f'O valor do salário reajustado é {salNovo}')
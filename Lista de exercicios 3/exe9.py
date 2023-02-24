minFarinha = 2
minOvos = 3
minLeite = 5
farinha = int(input("Digite a quantidade de farinha: "))
ovos = int(input("Digite a quantidade de ovos: "))
leite = int(input("Digite a quantidade de leite: "))

if farinha == (2*minFarinha) and ovos == (2*minOvos) and leite == (2*minLeite):
    print("É possível produzir 2 bolos")
elif farinha == minFarinha and ovos == minOvos and leite == minLeite:
    print("É possível produzir 1 bolo")
elif farinha > (2*minFarinha) and ovos > (2*minOvos) and leite > (2*minLeite):
    print("É possível fazer mais do que 2 bolos")
else:
    print("Não é possível fazer nenhum bolo")
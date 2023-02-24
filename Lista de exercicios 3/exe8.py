dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

bissexto = False
diaValido =  False
mesValido = False

if ano % 4 == 0:
    bissexto = True
else:
    bissexto = False

#Verificação de dias    
if mes == 2 and bissexto and dia <= 29:
    diaValido = True
elif mes != 2 and dia <= 30:
    diaValido =  True
else:
    diaValido =  False
#Verificação de mês
if mes > 0 and mes <= 12:
    mesValido = True
else:
    mesValido =  False

if diaValido and mesValido:
    print(f"A data {dia}/{mes}/{ano} é valida")
else:
    print(f"A data {dia}/{mes}/{ano} é inválida")
    

dias = int(input("Digite a quantidade de dias:"))
horas = int(input("Digite a quantidade de horas:"))
minutos = int(input("Digite a quantidade de minutos"))
segundos = int(input("Digite a quantidade de segundos"))

dias = dias*86400
horas = horas*3600
minutos = minutos*60 
segundos = segundos + dias + horas + minutos

print(f'O total de segundos é = {segundos}')
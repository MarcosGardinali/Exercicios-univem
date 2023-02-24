numPlaca = int(input("Digite o número da placa"))
finalPlaca = numPlaca%10
print(finalPlaca)

if finalPlaca == 1 or finalPlaca == 2:
    print("Segunda-Feira")
elif finalPlaca == 3 or finalPlaca == 4:
    print("Terça-Feira")
elif finalPlaca == 5 or finalPlaca == 6:
    print("Quarta-Feira")
elif finalPlaca == 7 or finalPlaca == 8:
    print("Quinta-Feira")
else:
    print("Sexta-Feira")

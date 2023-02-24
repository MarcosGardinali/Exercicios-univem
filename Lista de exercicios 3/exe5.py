trabalho = float(input("Digite a nota no trabalho: ")) 
avaliacao = float(input("Digite a nota na avaliação: "))
exame = float(input("Digite a nota no exame: "))

media = ((trabalho*2) + (avaliacao*3) + (exame*5))/10

if media > 0 and media <= 2.9:
    print(f"Aluno reprovado com a média {media:.2f}")
elif media >= 3 and media <= 4.9:
    print(f"Aluno de recuperação com a média {media:.2f}")
else: 
    print(f"Aluno aprovado com a média {media:.2f}")
    
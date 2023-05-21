media = float(input('Qual a nota? '))

if media > 7:
    situacao = "Aprovado"
elif media > 5:
    situacao = "Em recuperação"
else:
    situacao = "Reprovado"

print("Situação: " + situacao)

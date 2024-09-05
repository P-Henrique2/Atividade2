
quant_notas = int(input("Digite a quantidade de notas: "))
soma_notas = 0

for i in range(quant_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma_notas += nota

media = soma_notas / quant_notas

print("-----------------------")
print(f" MEDIA: {media:.1f}")
print("-----------------------")

if media >= 7:
    print(" ALUNO APROVADO ")
else:
    print(" ALUNO REPROVADO ")

print("-----------------------")

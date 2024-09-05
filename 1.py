
nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda Nota: "))
nota3 = float(input("Terceira Nota: "))
nota4 = float(input("Quarta Nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("-----------------------")
print(" ESCOLA CAVALO ALEGRE ")
print("-----------------------")

print(f" MEDIA: {media:.1f}")
print("-----------------------")

if media >= 7:
    print(" ALUNO APROVADO ")
else:
    print(" ALUNO REPROVADO ")

print("-----------------------")

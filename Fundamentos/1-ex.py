# Arquivo: ex10_media_turma_listas.py

qtd_alunos = int(input("Quantos alunos existem na turma? "))
notas = []

for i in range(qtd_alunos):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\nA média exata da turma é: {media:.2f}")
else:
    print("Nenhuma nota inserida.")
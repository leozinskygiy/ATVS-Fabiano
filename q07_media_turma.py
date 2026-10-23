"""
Sétima questão:
Pede cinco notas, soma todas elas e divide o resultado por 5 para calcular a média da turma.
"""

s = 0

for i in range(5):
    n = int(input("Digite a nota: "))
    s = s + n

m = s / 5
print(f"Média da turma: {m}")

"""
Décima questão:
Pede vários números, compara os valores vizinhos e troca suas posições quando necessário, deixando a lista em ordem crescente (Bubble Sort).
"""

n = int(input("Quantos números deseja digitar? "))

v = []

for i in range(n):
    va = int(input("Digite um número: "))
    v.append(va)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if v[j] > v[j + 1]:
            t = v[j]
            v[j] = v[j + 1]
            v[j + 1] = t

print(f"Vetor ordenado: {v} ")

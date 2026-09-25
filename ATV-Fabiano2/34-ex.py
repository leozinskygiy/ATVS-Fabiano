vetor = []
for i in range(5):
    val = input(f"Digite o {i+1}º valor: ")
    vetor.append(val)

print(f"\nOrdem original: {vetor}")

# Inversão usando manipulação de índices em laço de repetição
vetor_inverso = []
for i in range(len(vetor) - 1, -1, -1):
    vetor_inverso.append(vetor[i])

print(f"Ordem inversa: {vetor_inverso}")
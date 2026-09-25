vetor = []
for i in range(5):
    num = int(input(f"Digite o número para a posição {i}: "))
    vetor.append(num)

print("\n--- Posições e Valores ---")
for i, valor in enumerate(vetor):
    print(f"Posição {i}: Valor = {valor}")
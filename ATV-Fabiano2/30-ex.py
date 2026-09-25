frase = input("Digite uma frase: ")

# Contagem de palavras usando split() e laço
palavras = frase.split()
qtd_palavras = len(palavras)

# Contagem da letra 'A' ou 'a' usando laço de repetição
qtd_a = 0
for caractere in frase:
    if caractere.lower() == 'a':
        qtd_a += 1

print(f"\nQuantidade de palavras: {qtd_palavras}")
print(f"Quantidade de letras 'A'/'a': {qtd_a}")
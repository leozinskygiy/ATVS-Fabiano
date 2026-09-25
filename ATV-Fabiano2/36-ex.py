import random

# Gerando 8 números aleatórios entre 1 e 50
lista = [random.randint(1, 50) for _ in range(8)]
print(f"Lista gerada: {lista}")

busca = int(input("Digite um número para buscar na lista: "))

if busca in lista:
    posicao = lista.index(busca)
    print(f"O número {busca} está presente na posição {posicao}.")
else:
    print(f"O número {busca} não foi encontrado na lista.")
import random

# Vetor com 10 posições preenchidas com 0
caminho = [0] * 10

# Sorteia 3 posições únicas para colocar as minas (valor 1)
posicoes_minas = random.sample(range(10), 3)
for pos in posicoes_minas:
    caminho[pos] = 1

passos_dados = 0
vendeu = True

print("--- JOGO DO CAMINHO MINADO ---")
print("Escolha posições de 0 a 9 para pisar. Evite as 3 minas!")

posicoes_escolhidas = []

while passos_dados < 5:
    try:
        pos = int(input(f"\nPasso {passos_dados + 1}/5 - Escolha a posição (0-9): "))
        
        if pos < 0 or pos > 9:
            print("Posição inválida! Escolha entre 0 e 9.")
            continue
        if pos in posicoes_escolhidas:
            print("Você já pisou nessa posição! Escolha outra.")
            continue
            
        posicoes_escolhidas.append(pos)

        if caminho[pos] == 1:
            print(" BOOM! Você pisou em uma mina! Fim de jogo.")
            vendeu = False
            break
        else:
            print("Piso seguro! Continue em frente.")
            passos_dados += 1
            
    except ValueError:
        print("Digite um número inteiro válido.")

if vendeu:
    print("\n PARABÉNS! Você atravessou o caminho minado com sucesso!")
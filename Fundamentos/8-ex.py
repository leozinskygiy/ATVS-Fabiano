# Arquivo: ex03_validacao_segura.py

while True:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if 0 <= nota <= 10:
        print(f"Nota válida inserida: {nota}")
        break
    else:
        print("Erro: Nota inválida! Tente novamente.")
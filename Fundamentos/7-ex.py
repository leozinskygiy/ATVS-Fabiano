# Arquivo: ex04_somatorio_acumulado.py

soma = 0
while True:
    num = float(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    soma += num

print(f"Soma total: {soma}")
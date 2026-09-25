# Arquivo: ex06_filtro_pares.py

n = int(input("Digite um limite N: "))

print(f"Números pares entre 1 e {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
valor = int(input("Digite o valor do saque: R$ "))

# Cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 2, 1]

print("\n--- Cédulas Entregues ---")
for cedula in cedulas:
    qtd = valor // cedula
    if qtd > 0:
        print(f"{qtd} nota(s) de R$ {cedula}")
        valor %= cedula
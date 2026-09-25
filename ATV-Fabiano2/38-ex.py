numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\n--- Números Pares ---")
for num in numeros:
    if num % 2 == 0:
        print(num)
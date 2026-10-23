"""
Oitava questão:
Usa um laço while para percorrer os números de 1 a 50 e mostrar somente os números pares.
"""

n = 1

while n <= 50:
    if n % 2 == 0:
        print(f"{n}")
    n = n + 1

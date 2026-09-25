# Arquivo: ex09_sequencia_fibonacci.py

q = int(input("Quantos termos da sequência de Fibonacci deseja ver? "))

a, b = 0, 1
contador = 0

while contador < q:
    print(a, end=" " if contador < q - 1 else "\n")
    a, b = b, a + b
    contador += 1
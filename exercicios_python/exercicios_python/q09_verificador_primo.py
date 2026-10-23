"""
Nona questão:
Pede um número maior que 1 e verifica se ele é divisível por algum número entre 2 e ele mesmo, sem contar o próprio número.
"""

n = int(input("Digite um número maior que 1: "))
primo = True
i = 2

while i < n:
    if n % i == 0:
        primo = False
        break
    i += 1

if primo == False:
    print("Número não é primo")
else:
    print("Número É primo")

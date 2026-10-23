"""
Quarta questão:
Pede dois números e compara os valores para mostrar qual é o maior ou se eles são iguais.
"""

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n1 < n2:
    print(f"{n2} é maior a {n1}")
else:
    print(f"{n1} é igual {n2}")

"""
Quinta questão:
Pede três lados, verifica se eles formam um triângulo válido e classifica como equilátero, isósceles ou escaleno.
"""

a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    print("Triângulo válido — ")
    if a == b and b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Os lados não formam um triângulo válido")

# Arquivo: ex08_detector_primos.py

num = int(input("Digite um número: "))

if num <= 1:
    eh_primo = False
else:
    eh_primo = True
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print(f"O número {num} é PRIMO.")
else:
    print(f"O número {num} NÃO é primo.")
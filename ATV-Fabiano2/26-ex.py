# False indica poltrona vazia
poltronas = [False] * 10

while True:
    print("\n--- MAPA DE ASSENTOS ---")
    for i in range(10):
        status = "[X]" if poltronas[i] else f"[{i}]"
        print(status, end=" ")
    print("\n-----------------------")

    reserva = int(input("Digite o número da poltrona para reservar (0-9) ou negativo para sair: "))

    if reserva < 0:
        print("Encerrando sistema de reservas...")
        break

    if reserva >= 10:
        print("Poltrona inválida! Escolha de 0 a 9.")
        continue

    if poltronas[reserva]:
        print(" Status: Ocupada!")
    else:
        poltronas[reserva] = True
        print(" Status: Reservada com sucesso!")
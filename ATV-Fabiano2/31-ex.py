# Contadores: [1-João, 2-Maria, 3-José, 4-Nulo, 5-Branco]
votos = [0, 0, 0, 0, 0]

while True:
    print("\n--- URNA ELETRÔNICA ---")
    print("1- João | 2- Maria | 3- José | 4- Nulo | 5- Branco | 0- Encerrar")
    voto = int(input("Informe seu voto: "))

    if voto == 0:
        break
    elif 1 <= voto <= 5:
        votos[voto - 1] += 1
    else:
        print("Opção inválida! Tente novamente.")

print("\n--- RESULTADO FINAL ---")
candidatos = ["João", "Maria", "José", "Nulo", "Branco"]
for i in range(5):
    print(f"{candidatos[i]}: {votos[i]} voto(s)")

# Apuração dos candidatos (apenas índices 0, 1 e 2)
votos_candidatos = votos[:3]
maior_voto = max(votos_candidatos)

if votos_candidatos.count(maior_voto) > 1:
    print("\nHouve um EMPATE entre os candidatos mais votados!")
else:
    vencedor_idx = votos_candidatos.index(maior_voto)
    print(f"\nVencedor: {candidatos[vencedor_idx]} com {maior_voto} voto(s)!")
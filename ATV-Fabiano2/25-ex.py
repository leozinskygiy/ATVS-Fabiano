conta_criada = False
nome = ""
conta_num = ""
saldo = 0.0

while True:
    print("\n--- MINI-SISTEMA BANCÁRIO ---")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato / Ver Saldo")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Informe o nome do titular: ")
        conta_num = input("Informe o número da conta: ")
        saldo = float(input("Informe o saldo inicial: R$ "))
        if saldo < 0:
            saldo = 0.0
            print("Saldo inicial ajustado para R$ 0.00 (mínimo permitido).")
        conta_criada = True
        print(f"Conta criada com sucesso para {nome}!")

    elif opcao == '2':
        if not conta_criada:
            print("Erro: Crie uma conta antes de realizar operações!")
        else:
            deposito = float(input("Valor do depósito: R$ "))
            if deposito > 0:
                saldo += deposito
                print(f"Depósito de R$ {deposito:.2f} realizado!")
            else:
                print("Valor de depósito inválido.")

    elif opcao == '3':
        if not conta_criada:
            print("Erro: Crie uma conta antes de realizar operações!")
        else:
            saque = float(input("Valor do saque: R$ "))
            if saque <= 0:
                print("Valor de saque inválido.")
            elif saque <= saldo:
                saldo -= saque
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            else:
                print("Erro: Saldo insuficiente!")

    elif opcao == '4':
        if not conta_criada:
            print("Erro: Nenhuma conta foi criada ainda!")
        else:
            print("\n--- EXTRATO BANCÁRIO ---")
            print(f"Titular: {nome}")
            print(f"Conta: {conta_num}")
            print(f"Saldo Atual: R$ {saldo:.2f}")

    elif opcao == '5':
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
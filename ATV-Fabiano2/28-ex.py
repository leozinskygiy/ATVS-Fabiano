produtos = []
quantidades = []

while True:
    print("\n--- GERENCIADOR DE ESTOQUE ---")
    print("1 - Adicionar Produto")
    print("2 - Registrar Saída de Produto")
    print("3 - Ver Estoque")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade: "))
        if nome in produtos:
            idx = produtos.index(nome)
            quantidades[idx] += qtd
        else:
            produtos.append(nome)
            quantidades.append(qtd)
        print("Produto adicionado/atualizado!")

    elif opcao == '2':
        nome = input("Nome do produto para registrar saída: ")
        if nome in produtos:
            idx = produtos.index(nome)
            qtd_saida = int(input(f"Quantidade a retirar (Disponível: {quantidades[idx]}): "))
            
            if qtd_saida <= quantidades[idx]:
                quantidades[idx] -= qtd_saida
                print("Saída registrada com sucesso!")
            else:
                print("Erro: Estoque insuficiente!")
        else:
            print("Produto não encontrado!")

    elif opcao == '3':
        print("\n--- ESTOQUE ATUAL ---")
        if not produtos:
            print("Estoque vazio.")
        for i in range(len(produtos)):
            print(f"Produto: {produtos[i]} | Quantidade: {quantidades[i]}")

    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
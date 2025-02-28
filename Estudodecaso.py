estoque = []

def exibir_menu():
    print("\n=== Sistema de Controle de Estoque ===")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Visualizar Estoque")
    print("5. Ajustar Quantidade de Produto")
    print("6. Sair")

def obter_preco():
    while True:
        try:
            preco = float(input("Preço do produto: R$ "))
            if preco <= 0:
                raise ValueError("O preço deve ser um valor positivo.")
            return preco
        except ValueError:
            print("Por favor, insira um valor válido para o preço (somente números positivos).")

def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser um valor positivo.")
            return quantidade
        except ValueError:
            print("Por favor, insira um valor válido para a quantidade (somente números inteiros positivos).")

def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("O nome do produto não pode ser vazio.")
        return

    preco = obter_preco()
    quantidade = obter_quantidade()

    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Produto já existe no estoque. Use a opção de atualizar.")
            return

    estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print("Produto adicionado com sucesso!")

def atualizar_produto():
    nome = input("Nome do produto para atualizar: ").strip()

    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Produto encontrado! Insira os novos dados.")
            preco = obter_preco()
            quantidade = obter_quantidade()
            produto['preco'] = preco
            produto['quantidade'] = quantidade
            print("Produto atualizado com sucesso!")
            return

    print("Produto não encontrado no estoque.")

def excluir_produto():
    nome = input("Nome do produto para excluir: ").strip()

    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            estoque.remove(produto)
            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado no estoque.")

def ajustar_quantidade():
    nome = input("Nome do produto para ajustar a quantidade: ").strip()

    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print(f"Produto encontrado: {produto['nome']}, Quantidade atual: {produto['quantidade']}")
            while True:
                try:
                    ajuste = int(input("Informe a quantidade a ajustar (positivo para adicionar, negativo para remover): "))
                    if produto['quantidade'] + ajuste < 0:
                        print("Operação inválida. Não há estoque suficiente para essa remoção.")
                    else:
                        produto['quantidade'] += ajuste
                        print(f"Quantidade ajustada com sucesso! Nova quantidade: {produto['quantidade']}")
                        return
                except ValueError:
                    print("Por favor, insira um número válido para o ajuste.")
            return

    print("Produto não encontrado no estoque.")

def visualizar_estoque():
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("\n=== Estoque Atual ===")
        print(f"{'Nome':<20}{'Preço':<10}{'Quantidade':<10}")
        print("-" * 40)
        for produto in estoque:
            print(f"{produto['nome']:<20}R$ {produto['preco']:<10.2f}{produto['quantidade']:<10}")

def main():
    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            ajustar_quantidade()
        elif opcao == "6":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

from datetime import date

data = date.today()
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
ano, mes, dia = str(data).split("-")
mes = meses[int(mes) - 1]
print(dia, mes, ano)

for i in meses:
    exec(f"estoque{i}=open(f\"estoque de {i}.txt\",\"a\")")
    exec(f"vendas{i}=open(f\"vendas de {i}.txt\",\"a\")")

estoque = {}
fim = False
produtos = []


def n1():
    quantidade = input("Quantidade do produto: ")
    if quantidade.isnumeric() == False:
        print("-digite apenas numeros!-")
        n1()
    else:
        pass


def n2():
    preco = input("Preço do produto: ")
    if preco.isnumeric() == False:
        print("-digite apenas numeros!-")
        n2()
    else:
        pass


def programa():
    global estoque,fim,produtos,mes

    nomes = []
    precos = []
    estoques = []
    for i in meses:
        produtos_atual = open(rf'estoque de {i}.txt', 'r').readlines()
        if not not produtos_atual:  # verificar se não está vazia
            for produto in produtos_atual:
                separado = produto.strip().split(':')
                if 'produto' in separado:
                    nome_produto = separado[1]
                    nomes.append(nome_produto)

                if 'preço R$' in separado:
                    preco_produto = float(separado[1])
                    precos.append(preco_produto)

                if 'estoque' in separado:
                    estoque_produto = int(separado[1])
                    estoques.append(estoque_produto)

            estoque = {key: (value1, value2) for key, value1, value2 in zip(nomes, precos, estoques)}

    while not fim:
        print(
            "\nDigite 'fim' para finalizar\nDigite 'p' para exibir o estoque\nDigite 'c' para comprar algo do estoque\nDigite 'e' para adicionar no estoque")
        opcao = input("Opção:  ")

        if opcao == "e":
            produto = input("\nNome do produto: ")
            produtos.append(produto)
            quantidade = input("Quantidade do produto: ")
            # while
            if quantidade.isnumeric == False:
                n1()
            else:
                pass
            preco = input("Preço do produto: ")
            if preco.isnumeric == False:
                n2()
            else:
                pass

            quantidade = int(quantidade)
            preco = int(preco)

            estoque[produto] = [quantidade, preco]

            for i in meses:
                if i == mes:
                    exec(rf'estoque{i}.write(f"produto:{produto}\\npreço R$:{preco}\\nestoque:{quantidade}\\n\\n")')


        elif opcao == 'c':
            itens_disponiveis = []

            for i in estoque: itens_disponiveis.append(i)

            print(f'Produtos disponiveis: {", ".join(itens_disponiveis)}')

            if not itens_disponiveis:
                print('Não tem nenhum item no estoque!')
                programa()

            nome = input("Nome do produto: ")

            # Verificar se existe
            if nome not in itens_disponiveis:
                print('O item não existe!')
                programa()
            else:
                for i, j in enumerate(nomes):
                    if j==nome:
                        print(f'\t{nome} tem {estoques[i]} unidades no estoque.')

                    if j == nome:
                        print(f'\tPreço do {nome} = R${precos[i]}')


                    qtde = int(input("Quantidade a comprar: "))
                    #for i, j in enumerate(nomes):
                        #if j
                    if qtde <= estoques[i]:  # qtde < estoque
                        preco = qtde * estoques[i]  # preco
                        estoque[i] = estoques[i] - qtde

                        for i in meses:
                            if mes == i:

                                exec(rf"vendas{i}.write(f'produto:{produto}\nvalor R$:{preco}\nestoque:{qtde}\n\n')")


                        print(f'\nO total da compra deu R${preco}')
                        continuar = input('Deseja continuar? (S/N): ').lower()

                        if continuar == 's':
                            pass
                        elif continuar=='n':
                            break
                    else:
                        print('Coloque uma quantidade menor que o estoque')

        elif opcao == 'p':
            nomes = []
            precos = []
            estoques = []
            for i in meses:
                produtos_atual = open(rf'estoque de {i}.txt', 'r').readlines()
                if not not produtos_atual:  # verificar se não está vazia
                    for produto in produtos_atual:
                        separado = produto.strip().split(':')
                        if 'produto' in separado:
                            nome_produto = separado[1]
                            nomes.append(nome_produto)

                        if 'preço R$' in separado:
                            preco_produto = float(separado[1])
                            precos.append(preco_produto)

                        if 'estoque' in separado:
                            estoque_produto = int(separado[1])
                            estoques.append(estoque_produto)

                    estoque = {key: (value1, value2) for key, value1, value2 in zip(nomes, precos, estoques)}
                    print(estoque)



        elif opcao == "fim":
            fim = True
            print(estoque)
            break


programa()

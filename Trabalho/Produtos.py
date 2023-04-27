import csv


class Produtos:
    def __init__(self):
        self.listaProdutos = []

    # 📝 Passa produtos para a lista
    def registraItens(self, caminho: str):
        with open(caminho, "r") as file:
            reader = csv.reader(file)
            for linha in reader:
                self.listaProdutos.append(linha)

    def exibeTodosItens(self):
        for i in range(len(self.listaProdutos)):
            print(self.listaProdutos[i])

    # 👉 Opções

    def opcoes(self):
        print("Escolha uma opção:")
        print("1. Adicionar",
              "\n2. Exibir",
              "\n0. Sair")
        
    def menu(self):
        print("Esolha como exibir: ")
        print("1. Preço",
                    "\n2. Descrição",
                    "\n3. Estoque",
                    "\n0. Voltar")

    # 📚ORDENAÇÃO QUICK
    def ordenar(self, lista):
        def quicksort(lista):
            if len(lista) < 2:
                return lista

            pivo = lista[len(lista) // 2]

            esquerda = [x for x in lista if x < pivo]
            meio = [x for x in lista if x == pivo]
            direita = [x for x in lista if x > pivo]

            return quicksort(esquerda) + meio + quicksort(direita)

        return quicksort(lista)

    # ➕ Adicionar itens
    def adicionarItens(self, caminho: str, codigoProduto: str, nomeProduto: str, valorProduto: float, estoqueProduto: int):
        codigoProduto = codigoProduto.upper()
        with open(caminho, "w", newline="") as file:
            self.listaProdutos.append(
                [codigoProduto, nomeProduto, valorProduto, estoqueProduto])
            writer = csv.writer(file)
            for i in range(len(self.listaProdutos)):
                writer.writerow(self.listaProdutos[i])
            print("✅ Produto adicionado com sucesso!!!")

    # 💲 Ordenado por preço
    def ordenaPreco(self):
        listaTemporaria = []
        for i in range(len(self.listaProdutos)):
            valor = float(self.listaProdutos[i][2])
            listaTemporaria.append([valor])
            for j in range(len(self.listaProdutos[0])):
                if j != 2:
                    listaTemporaria[i].append(self.listaProdutos[i][j])

        listaTemporaria = self.ordenar(listaTemporaria)

        # for itens in listaTemporaria:
        #     print(itens)

        listaOrdenadaPrecos = []
        for l in range(len(listaTemporaria)):
            listaOrdenadaPrecos.append([])
            for m in range(len(listaTemporaria[0])):
                if m != 0:
                    listaOrdenadaPrecos[l].append(listaTemporaria[l][m])
                if m == 2:
                    listaOrdenadaPrecos[l].append(listaTemporaria[l][0])

        self.exibirListaOrdenada(listaOrdenadaPrecos, "Preço🔽")


    # 🪪 Ordenado por nome
    def ordenaNome(self):
        listaTemporaria=[]
        for i in range(len(self.listaProdutos)):
            valor=self.listaProdutos[i][1]
            listaTemporaria.append([valor])
            for j in range(len(self.listaProdutos[0])):
                if j != 1:
                    listaTemporaria[i].append(self.listaProdutos[i][j])

        listaTemporaria=self.ordenar(listaTemporaria)

        # for itens in listaTemporaria:
        #     print(itens)

        listaOrdenadaPrecos=[]
        for l in range(len(listaTemporaria)):
            listaOrdenadaPrecos.append([])
            for m in range(len(listaTemporaria[0])):
                if m != 0:
                    listaOrdenadaPrecos[l].append(listaTemporaria[l][m])
                if m == 1:
                    listaOrdenadaPrecos[l].append(listaTemporaria[l][0])

        self.exibirListaOrdenada(listaOrdenadaPrecos, "Descrição🔽")

    # 🔢 Ordenado por estoque

    def ordenaEstoque(self):
        listaTemporaria=[]
        for i in range(len(self.listaProdutos)):
            valor=int(self.listaProdutos[i][3])
            listaTemporaria.append([valor])
            for j in range(len(self.listaProdutos[0])):
                if j != 3:
                    listaTemporaria[i].append(self.listaProdutos[i][j])

        listaTemporaria=self.ordenar(listaTemporaria)

        # for itens in listaTemporaria:
        #     print(itens)

        listaOrdenadaPrecos=[]
        for l in range(len(listaTemporaria)):
            listaOrdenadaPrecos.append([])
            for m in range(len(listaTemporaria[0])):
                if m != 0:
                    listaOrdenadaPrecos[l].append(listaTemporaria[l][m])
                if m == 3:
                    listaOrdenadaPrecos[l].append(listaTemporaria[l][0])

        self.exibirListaOrdenada(listaOrdenadaPrecos, "Estoque🔽")

    def exibirListaOrdenada(self, lista, parametro):
        # Define a largura de cada coluna
        larguras = [8, 20, 15, 7]

        if (parametro == "Preço🔽"):
            celula01 = "Código"
            celula02 = "Descrição"
            celula03 = parametro
            celula04 = "Estoque"

        elif (parametro == "Descrição🔽"):
            celula01 = "Código"
            celula02 = parametro
            celula03 = "Preço"
            celula04 = "Estoque"

        elif (parametro == "Estoque🔽"):
            celula01 = "Código"
            celula02 = "Descrição"
            celula03 = "Preço"
            celula04 = parametro

    # Exibe o cabeçalho da tabela
        print("{:<{}}{:<{}}{:<{}}{:<{}}".format(
            ("\033[1m"+celula01+"  "), larguras[0], celula02, larguras[1], celula03, larguras[2], (celula04+"\033[0m"), larguras[3]))

        # print(" ")

        # Exibe cada produto como uma linha da tabela
        for produto in lista:
            print("{:<{}}{:<{}}{:<{}}{:<{}}".format(
                produto[0], larguras[0], produto[1], larguras[1], produto[2], larguras[2], produto[3], larguras[3]))

#   *1. inserir valores ✅
#  *2. exibir ordenado por preço
#  *3. exibir ordenado por nome
#  *4. exibir ordenado por quantidade no estoque

# todo  


registros=Produtos()
registros.registraItens("Trabalho/consulta.csv")

opcao = ""
menu = ""
registros.opcoes()
while opcao !=0:
    opcao = int(input(">>"))

    if opcao == 1:
        registros.adicionarItens("Trabalho/consulta.csv",
                                                str(input("Insira o código: ")), 
                                                str(input("Insira o produto: ")),
                                                float(input("Insira o preço: ")),
                                                int(input("Insira a quantidade: ")))
    elif opcao == 2:
        while menu != 0:
            registros.menu()
            menu = int(input(">>"))
            if menu == 1:
                # 💲
                registros.ordenaPreco()
            
            if menu == 2:
                # 🪪
                registros.ordenaNome()
            
            if menu == 3:
                # 🔢
                registros.ordenaEstoque()
    registros.opcoes()


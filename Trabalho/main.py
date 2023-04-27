import csv

listaProdutos = []

with open("Trabalho/consulta.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        listaProdutos.append(row)
    for i in range(len(listaProdutos)):
        print(listaProdutos[i])

# OPÇÕES


def opcoes():
    print("Escolha como quer ordenar os itens:")
    print("1. Preço",
          "\n2. Nome",
          "\n3. Estoque"
          "\n0. Sair")


# ✅ A INSERÇÃO DE PRODUTOS
# codigoProduto = "007"
# nomeProduto = "Um cone de rua"
# valorProduto = "0.50"
# estoqueProduto = "600"

# with open("04_Trabalho/consulta.csv", "w", newline="") as file:
#     listaProdutos.append(
#         [codigoProduto, nomeProduto, valorProduto, estoqueProduto])
#     writer = csv.writer(file)
#     for i in range (len(listaProdutos)):
#         writer.writerow(listaProdutos[i])
#     print("✅ Produto adicionado sem sucesso!!!")

# 📔ORDENAÇÃO QUICK
def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quicksort(left) + equal + quicksort(right)


# ➡️ORDENAÇÃO
opcao = ""
while opcao != 0:
    opcoes()
    opcao = input(">>")

    if opcao == '1':
        listaTemporaria = []
        for i in range(len(listaProdutos)):
            valor = float(listaProdutos[i][2])
            listaTemporaria.append([valor])
            for j in range (len(listaProdutos[0])):
                if j != 2:
                    listaTemporaria[i].append(listaProdutos[i][j])

        quicksort(listaTemporaria)
        for itens in listaTemporaria:
            print(itens)


'''
O que precisa fazer:
>>  Atualizar
>> Pesquisa (busca binária)
>> 
'''
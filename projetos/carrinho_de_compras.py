def criar_carrinho():
    return None 

def inserir_inicio(carrinho, item):
    return (item, carrinho)

def listar_itens(carrinho):
    aux = carrinho
    while aux is not None:
        print(aux[0])
        aux = aux[1]


def remover_item(carrinho, nomeItem):
    aux = carrinho
    novaLista = None 
    while aux is not None:
        nom = aux[0]
        if nom[0] != nomeItem:
            novaLista = (aux[0], novaLista)
        aux = aux[1]
    return novaLista

def calcular_total(carrinho):
    aux = carrinho
    total = 0
    while aux is not None:
        item = aux[0] 
        total += item[1] * item[2]
        aux = aux[1]
    return total 

carrinho = criar_carrinho()


while True:
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - Listar carrinho")
    print("4 - calcular total")
    print("5 - sair")
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        it = input("Digite o nome do item: ")
        qtd = int(input("Digite a quantidade do item: "))
        preco = float(input("Digite o valor do item: "))
        item = (it, qtd, preco)
        carrinho = inserir_inicio(carrinho, item)
    elif op == 2:
        nome = input("digite o nome do item a ser removido: ")
        carrinho = remover_item(carrinho, nome)
        print("item removido")
    elif op == 3:
        listar_itens(carrinho)
    elif op == 4:
        print("O valor total do carrinho é: {}".format(calcular_total(carrinho)))
    elif op == 5:
        break 

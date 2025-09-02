def criar_pilha():
    return {'topo': None}

def push(pilha, valor):
    no = {"prox": pilha['topo'],
          "ante": None,
          "val": valor}
    pilha['topo'] = no 
    return pilha

#Para essa é basicamente checar se o topo tá vazio, se tiver você já não precisa mais olhar os demais, talvez funcione tammbém para lista encadeada.
def isEmpty(pilha):  
    if pilha['topo'] == None:
        return None

#variavel aux recebe o primeiro valor da pilha, se ele não for none, vamos printando e pasando para o próximo, no caso, aux recebe a pilha em si.
def imprimir(pilha):
    aux = pilha['topo']
    while aux is not None:
        print(aux['val'])
        aux = aux['prox']

def tamanho(pilha):
    tam = 0 
    aux = pilha['topo']
    while aux is not None:
        tam += 1
        aux = aux['prox']
    return tam 

def peek(pilha):
    return pilha['topo']['val']

def pop(pilha):
    if pilha is None:
        return None 
    
    valor = pilha['topo']['val']
    pilha['topo'] = pilha['topo']['prox']

    return valor 

pilha = criar_pilha()
push(pilha, 10)
push(pilha, 20)
push(pilha, 30)

imprimir(pilha)
print(pop(pilha))





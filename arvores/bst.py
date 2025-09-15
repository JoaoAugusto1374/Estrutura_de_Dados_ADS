def criar_no(valor):
    return {"valor": valor, "esq": None, "dir": None}

def criar_arvore():
    return {"raiz": None}

def inserir(arvore, valor):
    no = criar_no(valor)

    if arvore['raiz'] is None:
        arvore['raiz'] = no 
    
    atual = arvore['raiz']
    while True:
        if valor < atual['valor']:
            if atual['esq'] is None:
                atual['esq'] = no 
                return
            else:
                atual = atual['esq']
        else:
            if atual['dir'] is None:
                atual['dir'] = no 
                return
            atual = atual['dir']
        
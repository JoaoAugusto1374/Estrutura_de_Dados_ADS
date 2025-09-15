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

def busca(arvore, valor):
    comeco = arvore['raiz'] #isso aqui é o começar na raiz, finalmente no fim da disciplina parece que o entendimento chega

    while comeco is not None: #isso aqui é verificar por sentinela até essa variável apontada ter o valor None.
        if valor == comeco['valor']: #não precisa voltar ao while nesse caso porque cada vez que ele assume o valor que está na esquerda ou direita ele verifica se não deu pan no None. Agora entenda como apontar para remover
            return True 
        elif valor < comeco['valor']:
            comeco = comeco['esq']
        elif valor > comeco['valor']:
            comeco = comeco['dir']
    return False


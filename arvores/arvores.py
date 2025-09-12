arvore = {
    "A": ["B", "C", "D"],
    "B": None,
    "C": ["E", "F"],
    "D": None,
    "E": None,
    "F": None
}

def obter_raiz(arvore):
    nos = set(arvore.keys())
    filhos = []
    for f in arvore.values():
        if f is not None:
            filhos.extend(f)
    return (nos - set(filhos)).pop()

print(obter_raiz(arvore))

def e_folha(arvore, no):
    return arvore[no] is None

def e_pai(arvore, no):
    return arvore[no] is not None 

#percorro cada valor presente nas chaves, os não nulos que estiverem na lista de valores 
#que é gerada na prática retornam true porque são filhos, os que não, retornam false
def e_filho(arvore, no):
    for f in arvore.values(): 
        if f is not None and no in f:
            return True 
    return False

print(e_filho(arvore, "A"))

def grau_no(arvore, no):
    filhos = arvore[no]
    if filhos is None:
        return 0
    return len(filhos)

print(grau_no(arvore, "A"))

def altura(arvore, no):
    if arvore[no] is None:
        return 0
    else:
        maior = 0
        for filho in arvore[no]:
            h = altura(arvore, filho)
            if h > maior:
                maior = h
        return 1 + maior
    
raiz = obter_raiz(arvore)
print(altura(arvore, raiz))
    
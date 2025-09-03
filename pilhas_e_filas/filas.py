def criar_fila():
    return {"inicio": None, "fim": None}

def push(fila, valor):
    no = {
        "prox": None, 
        "ante": fila['fim'], 
        "val": valor
    }


    if fila['inicio'] is None:
        fila['inicio'] = fila['fim'] = no 
    else: 
        fila['fim']['prox'] = no
    fila['fim'] = no

    return fila 

def imprimir(fila):
    aux = fila['inicio']
    while aux is not None:
        print(aux['val'])
        aux = aux['prox']

fila = criar_fila()
push(fila, 10)
push(fila, 20)
push(fila, 40)

imprimir(fila)

def tamanho(fila):
    tam = 0 
    aux = fila['inicio']
    while aux is not None:
        tam += 1
        aux = aux['prox']

def front(fila):
    return fila['inicio']

def last(fila):
    return fila['fim']

def dequeue(fila):
    if fila['inicio'] is None:
        return None 
    valor = fila['inicio']['val']
    fila['inicio'] = fila['inicio']['prox']
    if fila['inicio'] is None:
        fila['fim'] = None
    return valor
lista = {
    'inicio': None,
    'fim': None
}
def append(lista, valor):
    novo_no = {
        'valor':valor,
        'proximo': None,
        'anterior': None
    }
    if lista['inicio'] is None:
        lista['inicio'] = lista['fim'] = novo_no
    else:
        novo_no['anterior'] = lista['fim']
        lista['fim']['proximo'] = novo_no
        lista['fim'] = novo_no
append(lista, 10)
append(lista,20)
append(lista,30)

def contar(lista):
    atual = lista['inicio']
    cont = 0
    while atual is not None:
        cont += 1
        atual = atual['proximo']
    return cont 

print(contar(lista))

def buscar_indice(lista, indice):
    atual = lista['inicio']
    cont = 0
    while atual is not None:
        if cont == indice:
            return atual['valor']
        cont += 1    
        atual = atual['proximo']
    return "indice fora da lista"

print(buscar_indice(lista, 4))

def verificarValor(lista, valor):
    atual = lista['inicio']
    while atual is not None:
        if valor == atual['valor']:
            return "Valor existe na lista"
        atual = atual['proximo']
    return "valor fora da lista"

print(verificarValor(lista, 30))

def apagar_elemento(lista, pos):
    atual = lista['inicio']
    cont = 0
    while atual is not None:
        if pos == cont:
            if atual['anterior'] is None and atual['proximo'] is None:
                lista['inicio'] = lista['fim'] = None
            elif atual['anterior'] is None:
                lista['inicio'] = atual['proximo']
                atual['proximo']['anterior'] = None 
            elif atual['proximo'] is None:
                atual['anterior']['proximo'] = None
            else:
                atual['anterior']['proximo'] = atual['proximo']
                atual['proximo']['anterior'] = atual['anterior']
        atual = atual['proximo']
        cont += 1
    return lista 

apagar_elemento(lista, 0)

def imprimir(lista):
    atual = lista['inicio']
    while atual is not None:
        print(atual['valor'])
        atual = atual['proximo']

imprimir(lista)
    
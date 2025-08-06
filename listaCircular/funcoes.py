def criar_lista():
    return {'inicio': None, 'fim': None}
lista = criar_lista()

def inserir_Fim(lista, valor):
    no = {
        'valor': valor
    }

    if lista['inicio'] is None:
        no['proximo'] = no
        lista['inicio'] = lista['fim'] = no
    else:
        no['proximo'] = lista['inicio'] 
        lista['fim']['proximo'] = no
        lista['fim'] = no

inserir_Fim(lista,1)
inserir_Fim(lista,2)



def imprimir(lista):
    atual = lista['inicio'] 

    while True:
        print(atual['valor'])
        atual = atual['proximo']
        if atual == lista['inicio']:
            break
imprimir(lista)


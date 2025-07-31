lista = (1, (2, (3, None))) 

def contar_valores(lista, valor):
    cont = 0
    nova = lista
    while nova is not None:
        val = nova[0]
        if val > valor:
            cont += 1
        nova = nova[1]
    return cont 

print(contar_valores(lista, 2))

def inverter_lista(lista):
    nova = lista 
    novinha = None
    while nova is not None:
        novinha = (nova[0],novinha)
        nova = nova[1]
    
    return novinha
    
print(inverter_lista(lista))

def remover_todos_X(lista, valor):
    nova = lista
    novinha = None 
    while nova is not None:
        if valor != nova[0]:
            novinha = (nova[0], novinha)
        
        nova = nova[1]
    return inverter_lista(novinha )

print(remover_todos_X(lista, 2))

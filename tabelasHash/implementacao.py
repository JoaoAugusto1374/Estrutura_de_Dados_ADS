buckets = tuple([] for _ in range(10))

tabela_hash = {'buckets': buckets, 'capacidade': 10, 'elementos': 0}

def hash(s, c):
    soma = 0
    for l in s:
        soma += ord(l)
    return soma % c 

def adicionar(tabela, chave, valor):
    index = hash(chave, tabela_hash['capacidade']) #encontrar o inidice

    for (k, v) in tabela['buckets'][index]: #percorrer cada chave e valor nos baldes
        if k == chave:                      # se a chave que encontramos for igual a que será adicionada
            tabela['buckets'][index] = (chave, valor) #só atualizo o valor existente, é como se eu substituisse na verdade
            return tabela   # já retorna a tabela para não aumentar
    
    tabela['buckets'][index].append((chave, valor))
    tabela['elementos'] += 1
    return tabela 

adicionar(tabela_hash, "SAULO",1234)
adicionar(tabela_hash, "OSULA",9999)

def existe(tabela, chave, valor):
    index = hash(chave, tabela_hash['capacidade']) 
    return (chave, valor) in tabela['buckets'][index] 

print(existe(tabela_hash, "SAULO", 1234))

def recuperar(tabela, chave):
    index = hash(chave, tabela_hash['capacidade'])
    
    for (k, v) in tabela['buckets'][index]:
        if k == chave:
            return v 
    return None 

print(recuperar(tabela_hash, "SAULO"))

def apagar(tabela, chave, valor):
    index = hash(chave, tabela_hash['capacidade'])

    for i, (k, v) in enumerate(tabela['buckets'][index]):
        if (k, v) == (chave, valor):
            tabela['buckets'][index].pop(i)
            tabela['elementos'] -= 1
            return tabela
    
    return tabela

print(apagar(tabela_hash, "SAULO", 1234))
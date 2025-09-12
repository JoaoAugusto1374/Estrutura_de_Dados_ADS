buckets = tuple([] for _ in range(10))

tabela_hash = {'buckets': buckets, 'capacidade': 10, 'elementos': 0}

def hash(s, c):
    soma = 0
    for l in s:
        soma += ord(l)
    return soma % c 

def adicionar(tabela, chave, valor):
    index = hash(chave, tabela_hash['capacidade']) #encontrar o inidice

    for i, (k, v) in enumerate(tabela['buckets'][index]): #percorrer cada chave e valor nos baldes
        if k == chave:                      # se a chave que encontramos for igual a que será adicionada
            tabela['buckets'][index][i] = (chave, valor) #só atualizo o valor existente, é como se eu substituisse na verdade
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

def rehash(tabela, limite):
    fc = tabela['elementos'] / tabela['capacidade']
    if fc > limite:
        nova_capacidade = tabela['capacidade'] * 2
        novos_baldes = tuple([] for _ in range(nova_capacidade))

        for balde in novos_baldes:
            for(chave, valor) in balde:
                index = hash(chave, nova_capacidade)
                novos_baldes[index].append((chave, valor))
        
        tabela['buckets'] = novos_baldes
        tabela['capacidade'] = nova_capacidade

def add_word(tabela, palavra, sinonimos):
    index = hash(palavra, tabela['capacidade'])
    
    for i, (c, v) in enumerate(tabela['buckets'][index]):
        if c == palavra:
            tabela['buckets'][index][i] = (palavra, sinonimos)
            return tabela 
    tabela['buckets'][index].append((palavra, sinonimos))
    return tabela 

def add_sinonimo(tabela, chave, novoSinonimo):
    index = hash(chave, tabela['capacidade'])

    for i, (c, v) in enumerate(tabela['buckets'][index]):
        if c == chave:
            tabela['buckets'][index][i] = (chave, v + novoSinonimo)
            return tabela 
    return tabela

def getSinonimos(tabela, chave):
    index = hash(chave, tabela['capacidade']) 

    for (c, v) in tabela['buckets'][index]:
        if c == chave:
            return v 
    return chave 

def shrink(tabela, limite):
    fc = tabela['elementos'] / tabela['capacidade']
    if fc < limite:
        nova_capacidade = tabela['capacidade'] / 2
        novos_baldes = tuple([] for _ in range(nova_capacidade))

        for balde in novos_baldes:
            for (chave, valor) in balde:
                index = hash(chave, nova_capacidade)
                novos_baldes[index].append((chave, valor))
        tabela['buckets'] = novos_baldes
        tabela['capacidade'] = nova_capacidade

def frequencia(tabela, chave, frase):
    adicionar(tabela, chave, frase)
    index = hash(frase, tabela['capacidade'])

    for i, (chave, frase) in enumerate(tabela['buckets'][index]):
        palavras = frase.split()
        contagem = {}
        for palavra in palavras:
            contagem[palavra] = contagem.get(palavra, 0) + 1

        for palavra, cont in contagem.items():
            if cont > 1:
                print(f"A palavra '{palavra}' se repete {cont} vezes.")

frequencia(tabela_hash, "FRASE", "hash hash tabela tabela")
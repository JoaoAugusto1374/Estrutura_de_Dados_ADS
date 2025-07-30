from collections import namedtuple
Carrinho = namedtuple("Carrinho", ["itens", "frete", "cupom"])
Itens = namedtuple("Itens", ["descricao", "qtd", "preco"])
carrinho = Carrinho([], 30, 5)
item1 = Itens("bom", 3, 30)
item2 = Itens("ruim", 2, 15)
carrinho.itens.append(item1)
carrinho.itens.append(item2)

def checkout(c: Carrinho) -> float:
    total = 0
    for item in c.itens:
        total += item.qtd * item.preco
    return total 
print(checkout(carrinho))

def contar(c: Carrinho) -> int:
    qtd = 0
    for item in c.itens:
        qtd += 1
    return qtd

print(contar(carrinho))

def venda_total(c: Carrinho) -> float:
    valorComDesconto = checkout(carrinho) - (5/100 * checkout(carrinho))
    valorFinal = valorComDesconto - c.frete
    return valorFinal

print(venda_total(carrinho))

def imprimir_linha(c: Carrinho) -> str:
    preencher = "-" * 20
    frete = c.frete
    desconto = c.cupom / 100 * checkout(carrinho)
    total = venda_total(carrinho)
    print(f"frete {preencher} R${frete}")
    print(f"desconto {preencher} R${desconto}")
    print(f"total {preencher} R${total}")
imprimir_linha(carrinho)   
        



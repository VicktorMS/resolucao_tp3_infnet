transacoes = [
    "001,Teclado Gamer,2,150.00",
    "002,Mouse Sem Fio,5,75.50",
    "003,Monitor 24',1,800.00",
    "004,Notebook i5,3,3500.00",
    "005,Cadeira Ergonomica,1,1200.00",
    "006,Fone de Ouvido Bluetooth,4,250.00",
    "007,SSD 500GB,2,400.00",
    "008,HD Externo 1TB,1,350.00",
    "009,Cooler para CPU,3,100.00",
    "010,Placa de Vídeo RTX 3060,1,4500.00"
]

def calcular_vendas(transacoes):
    vendas_totais = []
    for transacao in transacoes:
        id_produto, nome_produto, quantidade, valor_unitario = transacao.split(",")
        valor_total = int(quantidade) * float(valor_unitario)
        vendas_totais.append((id_produto, nome_produto, int(quantidade), valor_total))
    return vendas_totais

def converter_moeda(vendas_totais, fator_conversao):
    vendas_convertidas = []
    for venda in vendas_totais:
        _, nome_produto, _, valor_total = venda
        valor_convertido = valor_total * fator_conversao
        vendas_convertidas.append((nome_produto, valor_convertido))
    return vendas_convertidas

def produto_mais_vendido(vendas_totais):
    mais_vendido = vendas_totais[0] 
    for venda in vendas_totais:
        if venda[2] > mais_vendido[2]:  
            mais_vendido = venda
    return mais_vendido

def produto_maior_receita(vendas_totais):
    maior_receita = vendas_totais[0]
    for venda in vendas_totais:
        if venda[3] > maior_receita[3]:  
            maior_receita = venda
    return maior_receita

vendas_totais = calcular_vendas(transacoes)
mais_vendido = produto_mais_vendido(vendas_totais)
maior_receita = produto_maior_receita(vendas_totais)

fator_conversao = float(input("Digite o fator de conversão para a nova moeda: "))
vendas_convertidas = converter_moeda(vendas_totais, fator_conversao)

for venda in vendas_totais:
    print(f"Produto: {venda[1]}, Quantidade Vendida: {venda[2]}, Valor Total: {venda[3]:.2f}")

print(f"\nProduto mais vendido: {mais_vendido[1]} (Quantidade: {mais_vendido[2]})")
print(f"Produto com maior receita: {maior_receita[1]} (Receita: R${maior_receita[3]:.2f})\n\n")
print("="*5, "Valores com conversão de Moeda", "="*5, '\n')
for venda in vendas_convertidas:
    nome_produto, valor_convertido = venda
    print(f"Produto: {nome_produto}, Valor de Vendas totais Convertido: {valor_convertido:.2f}")
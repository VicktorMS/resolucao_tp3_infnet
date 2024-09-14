#"ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário",
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

maior_venda = 0
idx_maior_venda = 0
for i in range(len(transacoes)):
    transacao = transacoes[i].split(",")
    valor_total = int(transacao[2]) * float(transacao[3])
    if valor_total > maior_venda:
        maior_venda = valor_total
        idx_maior_venda = i
    transacao.append(str(valor_total))
    transacoes[i] = ",".join(transacao)


print(transacoes)
print(transacoes[idx_maior_venda])
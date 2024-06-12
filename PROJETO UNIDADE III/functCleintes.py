def lancheCarrinho(precoLanche, lanche, email, escolhaCliente, carrinhoCliente, carrinhos):
    escolhaCliente.append(precoLanche) # [2]
    escolhaCliente.append(lanche) # [3]
    carrinhoCliente.append(escolhaCliente)
    carrinhos[email] = carrinhoCliente
    print('Combo adicionado ao carrinho')
    print('Obrigado! Vá ao carrinho para confirmar a compra!')


def lancheCarrinho(precoLanche, lanche, email, carrinhoCliente, carrinhos):
    carrinhoCliente.append(precoLanche) # [2]
    carrinhoCliente.append(lanche) # [3]
    carrinhos[email] = carrinhoCliente
    print('Combo adicionado ao carrinho')
    print('Obrigado! Vá ao carrinho para confirmar a compra!')


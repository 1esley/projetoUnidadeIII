def lancheCarrinho(precoLanche, lanche, email, escolhaCliente, carrinhoCliente, carrinhos):
    escolhaCliente.append(precoLanche) # [2]
    escolhaCliente.append(lanche) # [3]
    carrinhoCliente.append(escolhaCliente)
    carrinhos[email] = carrinhoCliente
    print('Combo adicionado ao carrinho')
    print('Obrigado! Vá ao carrinho para confirmar a compra!')

def trocarSenhaCliente(email, clientes):
    while True:
        emailTrocaDeSenhaCliente = input('Insira o seu email: ').lower()
        senhaAntigaCliente = input('Insira sua senha atual: ')
        if (emailTrocaDeSenhaCliente in clientes) and (clientes[emailTrocaDeSenhaCliente] == senhaAntigaCliente): # só troca a senha se fizer login
            novaSenhaCliente = input('Insira a nova senha: ')
            if emailTrocaDeSenhaCliente == email: # verifica se o email insirdo é o mesmo que está logado
                clientes[email] = novaSenhaCliente
                print(('#'*30) +'\n SUA SENHA FOI ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                break
            break
        else:
            print('Email ou senha inválidos.')
            continue

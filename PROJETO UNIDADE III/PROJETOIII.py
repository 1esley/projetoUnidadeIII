import os
import enviarEmail
import functCleintes
import functAdmins

def calcularPagamento(pagouNo, comLanche):
    if pagouNo == 'PIX':
        if comLanche:
            valorPagamento = precoTotalComLanche * 0.85
            precoTotalPrint = precoTotalComLanche
        else:
            valorPagamento = precoTotalSemLanche * 0.85
            precoTotalPrint = precoTotalSemLanche
    elif pagouNo == 'Cartão de débito':
        if comLanche:
            valorPagamento = precoTotalComLanche * 0.95
            precoTotalPrint = precoTotalComLanche
        else:
            valorPagamento = precoTotalSemLanche * 0.95
            precoTotalPrint = precoTotalSemLanche
    elif pagouNo == 'Cartão de crédito':
        if comLanche:
            valorPagamento = precoTotalComLanche * 1.05
            precoTotalPrint = precoTotalComLanche
        else:
            valorPagamento = precoTotalSemLanche * 1.05
            precoTotalPrint = precoTotalSemLanche

    return valorPagamento, precoTotalPrint

clientes = {}
admins = {}
filmes = []
carrinhos = {}
livre = True
ocupado = False
statusSala1 = livre
statusSala2 = livre
statusSala3 = livre
filmeOcupante = None
infosSala1 = [filmeOcupante, statusSala1]
infosSala2 = [filmeOcupante, statusSala2]
infosSala3 = [filmeOcupante, statusSala3]
qtdIngressosCompra = 0
semCarrinho = True
clienteEncontrado = False
filmeEncontradoADM = False
filmeEncontradoCliente = False
while True: # while menu principal
    print('='*30 + '# CINE SERTÃO - MENU PRINCIPAL #' + '='*30)
    opcaoMenuPrincipal = input('Escolha uma das opções abaixo.\n[1] Fazer login como ADM\n[2] Fazer login como cliente\n[3] Cadastrar usuário\n[0] Finalizar programa\nEscolha uma opção: ')
    # ^-- variavel que contém o menu principal e a escolha do usuario
    if opcaoMenuPrincipal == '1':
        nomeUser = input('Insira o nome pelo qual gostaria de ser chamado hoje: ')
        email = input('Insira seu email: ').lower()
        senha = input('Insira sua senha: ')
        
        if (email in admins) and (admins[email] == senha): #verificar se o email está cadastrado, e se a senha inserida é exatamente igual a senha associada ao email cadastrado.
            print('~'*40 + f'\nSeja bem vindo, ADM {nomeUser}\n' + '~'*40)
            while True:
                print('='*30 + '# MENU DE ADM #' + '='*30)
                print('-'*15 + f'| ADM LOGADO: {nomeUser} |' + '-'*15)
                opcaoMenuADM = input('[1] Cadastrar filme\n[2] Buscar filme\n[3] Buscar cliente\n[4] Outras opções\n[0] Voltar ao menu principal\nEscolha uma opção: ')
                # ^-- variavel que contém o menu do adm e sua escolha

                if opcaoMenuADM == '1':
                    functAdmins.funcCadastrarFilme(infosSala1, infosSala2, infosSala3, ocupado, filmes)
                elif opcaoMenuADM == '2':
                    while True: # while menu busca de filmes
                        naoRemovido = True
                        if len(filmes) == 0:
                            print('Não há nenhum filme cadastrado.')
                            break
                        print('='*30 + '# BUSCAR FILMES #' + '='*30)

                        for filme in filmes:
                            print(f'Filme: {filme[0]}', f'| Preço: R${filme[5]}', f'| Sala: {filme[2]}', f'| Ingressos disponíveis: {filme[3]}', f'| Duração: {filme[1]} min', f'| Horário: {filme[4]}', f'| Autor: {filme[6]}', end=' | \n')
                        
                        buscaFilme = input('Digite o nome do Filme que deseja buscar ou 0 para voltar ao menu anterior: ').upper()
                        if buscaFilme == '0':
                            break
                        for filme in filmes: # busca cada lista nas listas de filme
                            if buscaFilme == filme[0]: # compara o nome buscado com o nome da lista (indice 0 corresponde ao nome)
                                filmeEncontradoADM = True
                                print('Filme encontrado.')
                                                                                             
                        if filmeEncontradoADM:
                            while naoRemovido:
                                opcaoMenuBuscaFilme = input(f'O que deseja fazer com o filme {buscaFilme}?\n[1] Atualizar o filme {buscaFilme}\n[2] Remover o filme {buscaFilme}\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
                                if opcaoMenuBuscaFilme == '1':
                                    functAdmins.funcAtualizarFilme(buscaFilme, infosSala1, infosSala2, infosSala3, livre, ocupado, qtdIngressosCompra, filme)

                                elif opcaoMenuBuscaFilme == '2':
                                    print('='*30 + '# REMOVER FILME #' + '='*30)
                                    if filme[3] != filme[7]: # verifica se o numero de ingressos disponiveis é difrente da capacidade
                                        print(f'Não é possível remover esse filme.\nIngressos para o filme {buscaFilme} já foram vendidos.')
                                        break
                                    else:
                                        while True:
                                            certeza = input(f'Tem certeza que deseja remover o filme {buscaFilme}?\n(s/n): ').lower()
                                            if certeza == 's':
                                                print(('#'*30) +'\nFILME REMOVIDO COM SUCESSO\n'+ ('#'*30))
                                                naoRemovido = False
                                                for x in range(3):
                                                    if filme[0] == infosSala1[0]:
                                                        infosSala1[1] = livre
                                                    elif filme[0] == infosSala2[0]:
                                                        infosSala2[1] = livre
                                                    elif filme[0] == infosSala3[0]:
                                                        infosSala3[1] = livre
                                                    
                                                filmes.remove(filme)
                                                break
                                            
                                            elif certeza == 'n':
                                                print('\nRemoção de filme cancelada\n')
                                                break
                                            else:
                                                print('Opção inválida.')
                                                continue
                                elif opcaoMenuBuscaFilme == '0':
                                    break
                                else:
                                    print('Opção inválida.')
                                    continue
                        else:
                            print('Filme não encontrado. Verifique se a busca foi feita corretamente ou se o filme existe.')

                elif opcaoMenuADM == '3':
                    while True:
                        naoRemovidoCliente = True
                        if len(clientes) == 0:
                            print('Nenhum cliente cadastrado.')
                            break
                        print('='*30 + '# BUSCAR CLIENTE #' + '='*30)
                        for cliente in clientes:
                                print(f'Email: {cliente}', end=' | \n')
                        emailBuscaCliente = input('Insira o email do cliente que deseja buscar: ')
                        for cliente in clientes:
                            if emailBuscaCliente == cliente:
                                print('Cliente encontrado.')
                                clienteEncontrado = True # controle do if que roda a busca do cliente
                                
                        if clienteEncontrado:
                            while naoRemovidoCliente:
                                opcaoMenuBuscaCliente = input(f'O que deseja fazer com o cliente {emailBuscaCliente}?\n[1] Atualizar dados do cliente\n[2] Remover o cliente\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
                                if opcaoMenuBuscaCliente == '1':
                                    functAdmins.funcAtualizarDadosCliente(emailBuscaCliente, clientes)
                                        
                                elif opcaoMenuBuscaCliente == '2':
                                    while True:
                                        print('='*30 + '# REMOVER CLIENTE #' + '='*30)
                                        certeza = input(f'Tem certeza que deseja remover o cliente {emailBuscaCliente}?\n(s/n): ').lower()
                                        if certeza == 's':
                                            del clientes[emailBuscaCliente]
                                            print(('#'*30) +'\nCLIENTE REMOVIDO COM SUCESSO\n'+ ('#'*30))
                                            naoRemovidoCliente = False
                                            break
                                        elif certeza == 'n':
                                            print('\nRemoção de cliente cancelada\n')
                                            break
                                        else:
                                            print('Opção inválida.')
                                            continue
                                elif opcaoMenuBuscaCliente == '0':
                                    break

                                else:
                                    print('Opção inválida.')
                                    continue
                        else:
                            print('Cliente não encontrado. Verifique se a busca foi feita corretamente ou se o cliente está cadastrado.')

                elif opcaoMenuADM == '4':
                    while True:
                        print('='*30 + '# OUTRAS OPÇÕES #' + '='*30)
                        opcaoOutrasOpcoes = input('[1] Atualizar nome de usuário\n[2] Trocar senha de admin\n[3] Atualizar email\n[4] Listar ingressos vendidos\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
                        if opcaoOutrasOpcoes == '1':
                                print('='*30 + '# ATUALIZAR NOME DE USUÁRIO #' + '='*30)
                                print(f'Seu nome de usuário atual é {nomeUser}.')
                                novoNomeUserADM = input('Insira seu novo nome de usuário: ')
                                if novoNomeUserADM.isdigit(): # verifica se é um nome alfabético
                                    print('Por favor, utilize apenas carateres alfabéticos.')
                                else:
                                    nomeUser = novoNomeUserADM
                                    print(('#'*30) +'\n NOME DE USUÁRIO ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                    break
                        elif opcaoOutrasOpcoes == '2':
                            print('='*30 + '# TROCAR SENHA DE ADM #' + '='*30)
                            print('-'*15 + '| FAÇA LOGIN PARA CONTINUAR |' + '-'*15)
                            while True:
                                emailTrocaDeSenhaADM = input('Insira o seu email: ').lower()
                                senhaAntigaADM = input('Insira sua senha atual: ')
                                if (emailTrocaDeSenhaADM in admins) and (admins[emailTrocaDeSenhaADM] == senhaAntigaADM): # só troca a senha se fizer login antes
                                    novaSenhaADM = input('Insira a nova senha: ')
                                    if emailTrocaDeSenhaADM == email: # verifica se o email inserido é o mesmo que está logado
                                        admins[email] = novaSenhaADM
                                        print(('#'*30) +'\n SUA SENHA FOI ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                        break
                                    else:
                                        print('Email inserido difere do email logado.')
                                    break
                                else:
                                    print('Email ou senha inválidos.')
                                    continue
                        elif opcaoOutrasOpcoes == '3':
                            print('='*30 + '# ATUALIZAR EMAIL DE ADM #' + '='*30)
                            print('-'*15 + '| FAÇA LOGIN PARA CONTINUAR |' + '-'*15)
                            while True:
                                emailTrocaDeEmailADM = input('Insira seu email atual: ').lower()
                                senhaTrocaDeEmailADM = input('Insira sua senha: ')
                                if (emailTrocaDeEmailADM in admins) and (admins[emailTrocaDeEmailADM] == senhaTrocaDeEmailADM): # só troca o email se fizer login antes
                                    novoEmailADM = input('Insira o seu novo email: ').lower()
                                    if emailTrocaDeEmailADM == email: # verifica se o email inserido é o mesmo email logado
                                        admins[novoEmailADM] = admins[emailTrocaDeEmailADM] 
                                        del admins[emailTrocaDeEmailADM]
                                        print(('#'*30) +'\nEMAIL ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                        break
                                    else:
                                        print('Email inserido difere do email logado.')
                                    break

                        elif opcaoOutrasOpcoes == '4':
                            print('='*30 + '# INGRESSOS VENDIDOS #' + '='*30)
                            controlePrintIngressosVendidos = 0
                            for filme in filmes:
                                if filme[3] != filme[7]:                               
                                    print(f'Filme: {filme[0]}', f'| Ingressos vendidos: {filme[7] - filme[3]}', f'| Ingressos disponíveis: {filme[3]}', end=' | \n')
                                    controlePrintIngressosVendidos += 1
                            if controlePrintIngressosVendidos == 0:
                                print('Não foram vendidos ingressos para nenhum filme.')
                            ingressosVendidosArquivo = open('IngressosVendidos.txt', 'w')
                            ingressosVendidosArquivo.write('---------------------------- INGRESSOS VENDIDOS ----------------------------\n')
                            for filme in filmes:
                                if filme[3] != filme[7]:                               
                                    print(f'Filme: {filme[0]}', f'| Ingressos vendidos: {filme[7] - filme[3]}', f'| Ingressos disponíveis: {filme[3]}', end=' | \n', file=ingressosVendidosArquivo)
                            
                        elif opcaoOutrasOpcoes == '0':
                            break
                        else:
                            print('Opção inválida.')
                            continue

                elif opcaoMenuADM == '0':
                    break

                else:
                    print('Opção inválida.')
                    continue

        elif email in clientes: #verificar se o usuário é um cliente que quer acessar a aba de ADM's
            print("Você não tem permissão de acesso para a aba de ADM's")

        else:
            print('Email ou senha inválidos.') #imprimir mensagem que não deixa explícito qual dado inserido está correto.

    elif opcaoMenuPrincipal == '2':
        nomeUser = input('Insira o nome pelo qual gostaria de ser chamado hoje: ')
        email = input('Insira seu email: ').lower()
        senha = input('Insira sua senha: ')
        
        if (email in clientes) and (clientes[email] == senha): #verificar se o email está cadastrado, e se a senha inserida é exatamente igual a senha associada ao email cadastrado.
            print('~'*40 + f'\nSeja bem vindo, CLIENTE {nomeUser}\n' + '~'*40)
            carrinhoCliente = [] # cria o carrinho proprio do cliente
            
            while True:
                print('='*30 + '# MENU DE CLIENTES #' + '='*30)
                print('-'*15 + f'| CLIENTE LOGADO: {nomeUser} |' + '-'*15)
                opcaoMenuCliente = input('\nEscolha uma das opções abaixo.\n[1] Comprar ingresso\n[2] Carrinho\n[3] Editar perfil\n[0] Voltar para o menu principal\nEscolha uma opção: ')
                # ^-- variável que recebe o menu do cliente e a sua escolha
                if opcaoMenuCliente == '1':
                    print('='*30 + '# COMPRAR INGRESSO #' + '='*30)
                    if len(filmes) == 0:
                        print('Não há nenhum filme cadastrado para venda.')
                        continue
                    else:
                        print(f'Aqui estão os filmes disponíveis: ')
                        for filme in filmes:
                            print(f'Filme: {filme[0]}', f'| Preço: R${filme[5]}', f'| Sala: {filme[2]}', f'| Ingressos disponíveis: {filme[3]}', f'| Duração: {filme[1]} min', f'| Horário: {filme[4]}', f'| Autor: {filme[6]}', end=' | \n')
                        
                        filmeCompra = input('Insira o nome do filme que deseja comprar: ').upper()
                        for filme in filmes:
                            if filmeCompra == filme[0]: # compara o filme buscado com o indice 0 da lista de cada filme
                                filmeEncontradoCliente = True
                                filmeQueFoiEncontrado = filme
                            
                                                                                           
                        if filmeEncontradoCliente:
                            if filmeQueFoiEncontrado[3] >= 1: # verifica se ainda tem ingressos disponiveis para o filme escolhido
                                
                                escolhaCliente = []
                                while True:
                                    qtdIngressosCompra = int(input(f'Insira a quantidade e ingressos que deseja para o filme {filmeCompra}: '))
                                    if qtdIngressosCompra <= filmeQueFoiEncontrado[3]: # verifica se o cliente escolheu uma quantidade <= aos ingressos restantes para o filme
                                        filmeQueFoiEncontrado[3] -= qtdIngressosCompra
                                        valorIngressoCompradoCliente = filmeQueFoiEncontrado[5] * qtdIngressosCompra
                                        escolhaCliente.append(filmeQueFoiEncontrado[0]) # [0]
                                        escolhaCliente.append(valorIngressoCompradoCliente) # [1]
                                        
                                        print('Filme adicionado ao carrinho.')
                                        escolhasAfirmativas = ['s', 'sim', 'y', 'yes']
                                        escolhasNegativas = ['n', 'não', 'nao', 'no', 'not']
                                        escolhaComida = input('Deseja comprar algum lanche?\n(s/n): ').lower()
                                        if escolhaComida in escolhasAfirmativas:
                                            menuLanches = input('Escolha o combo que deseja.\n[1] Pipoca + Refri Coisa Nossa por R$ 9.99 \n[2] Hambúrguer + Refri GPFresco por R$ 11.99\n[3] Pipoca + MilkShake por R$ 14.99\nEscolha sua opção: ')
                                            # ^-- variável com o menu de combos de lanches e a escolha do cliente
                                            if menuLanches == '1':
                                                precoLanche = 9.99
                                                lanche = 'Combo Pipoca + Refri Coisa Nossa'
                                                functCleintes.lancheCarrinho(precoLanche, lanche, email, escolhaCliente, carrinhoCliente, carrinhos)
                                                break
                                            elif menuLanches == '2':
                                                precoLanche = 11.99
                                                lanche = 'Hambúrguer + Refri GPFresco'
                                                functCleintes.lancheCarrinho(precoLanche, lanche, email, escolhaCliente, carrinhoCliente, carrinhos)
                                                break
                                            elif menuLanches == '3':
                                                precoLanche = 14.99
                                                lanche = 'Combo Pipoca + MilkShake'
                                                functCleintes.lancheCarrinho(precoLanche, lanche, email, escolhaCliente, carrinhoCliente, carrinhos)
                                                break
                                    
                                        elif escolhaComida in escolhasNegativas:
                                            carrinhoCliente.append(escolhaCliente) # [0]
                                            carrinhos[email] = carrinhoCliente
                                            print('Obrigado! Vá ao carrinho para confirmar a compra!')
                                            break

                                        else:
                                            print('Opção inválida.')
                                    else:
                                        print(f'A quantidade de ingressos para esse filme é de {filme[3]}.\nPor favor, insira novamente a quantidade que deseja comprar.')
                            else:
                                print('Ingressos esgotados!')
                        else:
                            print('FILME NÃO ESTÁ EM CARTAZ, OU NOME BUSCADO ESTÁ INCORRETO.')
                        
                elif opcaoMenuCliente == '2':
                    while True:
                        print('='*30 + '# CARRINHO #' + '='*30)
                        print(f'Bem vindo ao seu carrinho, {nomeUser}!\nAqui estão os itens escolhidos:')
                        for cliente in carrinhos:
                            if cliente == email:
                                if escolhaComida in escolhasAfirmativas: # se quis comida exibe o preço do filme e do combo e armazena eles
                                    precoTotalComLanche = 0
                                    ingressosPorClienteArquivo = open('ingressosPorClienteArquivo.txt', 'w')
                                    ingressosPorClienteArquivo.write(f'---------------------------- INGRESSOS COMPRADOS ----------------------------\nCliente: {email}\n')
                                
                                    for escolha in carrinhoCliente:
                                        print('-' * 65 + f'\nFilme escolhido: {escolha[0]} | Valor do(s) ingresso(s): R$ {escolha[1]}\nLanche: {escolha[3]} | Preço do lanche: R$ {escolha[2]}\n' + '-' * 65)
                                        print('-' * 65 + f'\nFilme escolhido: {escolha[0]} | Valor do(s) ingresso(s): R$ {escolha[1]}\nLanche: {escolha[3]} | Preço do lanche: R$ {escolha[2]}\n' + '-' * 65, file=ingressosPorClienteArquivo)
                                        precoTotalComLanche += (escolha[1] + escolha[2])
                                    print(f'Preço total: R$ {precoTotalComLanche:.2f}')
                                    print(f'Preço total: R$ {precoTotalComLanche:.2f}', file=ingressosPorClienteArquivo)
                                    comLanche = True

                                else: # se não, só o filme
                                    precoTotalSemLanche = 0
                                    ingressosPorClienteArquivo = open('ingressosPorClienteArquivo.txt', 'w')
                                    ingressosPorClienteArquivo.write(f'---------------------------- INGRESSOS COMPRADOS ----------------------------\nCliente: {email}')
                                    for escolha in carrinhoCliente:
                                        print('-' * 65 + f'\nFilme escolhido: {escolha[0]} | Valor do(s) ingresso(s): R$ {escolha[1]:.2f}\n' + '-' * 65)
                                        print('-' * 65 + f'\nFilme escolhido: {escolha[0]} | Valor do(s) ingresso(s): R$ {escolha[1]:.2f}\n' + '-' * 65, file=ingressosPorClienteArquivo)
                                        precoTotalSemLanche += escolha[1]
                                    print(f'Preço total: R$ {precoTotalSemLanche:.2f}')
                                    print(f'Preço total: R$ {precoTotalSemLanche:.2f}', file=ingressosPorClienteArquivo)
                                    comLanche = False

                        confirmarCompra = input('Deseja confirmar sua compra?\n(Caso o carrinho esteja vazio, insira 0 para retornar ao menu de cliente.)\n(s/n/0): ')
                        if confirmarCompra == '0':
                            break
                        
                        elif confirmarCompra in escolhasAfirmativas:
                            print(('#'*30) +'\n PEDIDO CONFIRMADO \n'+ ('#'*30))
                            metodoDePagamento = input('Escolha o métoido de pagamento.\n[1] PIX (à vista - desconto de 15%)\n[2] Cartão de débito (à vista - desconto de 5%)\n[3] Cartão de crédito (à prazo - acréscimo de 5%)\nEscolha uma opção: ')
                            if metodoDePagamento == '1':
                                pagouNo = 'PIX'
                                desconto = '15%'
                                acrescimo = '0'
                                valorPagamento, precoTotalPrint = calcularPagamento(pagouNo, comLanche)
                                
                            elif metodoDePagamento == '2':
                                pagouNo = 'Cartão de débito'
                                desconto = '5%'
                                acrescimo = '0'
                                valorPagamento, precoTotalPrint = calcularPagamento(pagouNo, comLanche)

                            elif metodoDePagamento == '3':
                                pagouNo = 'Cartão de crédito'
                                desconto = '0'
                                acrescimo = '5%'
                                valorPagamento, precoTotalPrint = calcularPagamento(pagouNo, comLanche)
                            else:
                                print('Opção inválida.')

                            destinatario = email
                            enviarEmail.enviar_email(precoTotalPrint, pagouNo, desconto, acrescimo, valorPagamento, destinatario)
                            print('\nSUA NOTA FISCAL FOI ENVIADA VIA EMAIL CADASTRADO\n')
                            break
                    
                        elif confirmarCompra in escolhasNegativas:
                            print(('#'*30) +'\n PEDIDO CANCELADO \n'+ ('#'*30))
                            removerDoCarrinho = input('Deseja remover os itens do carrinho?\n(s/n): ')
                            if removerDoCarrinho in escolhasAfirmativas:
                                for cliente in carrinhos:
                                    if cliente == email:
                                        del carrinhos[cliente]
                                        print(('#'*30) +'\nCARRINHO REMOVIDO\n'+ ('#'*30))
                                        break
                                    break
                            else:
                                print('Retornando ao menu do cliente.')
                                break
                        else:
                            print('Opção inválida.')

                elif opcaoMenuCliente == '3':
                    while True:
                        print('='*30 + '# EDITAR PERFIL #' + '='*30)
                        editarPerfilCliente = input('Escolha a alteração que deseja fazer.\n[1] Atualizar nome de usuário\n[2] Trocar senha\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
                        # ^-- variável que recebe o menu de editar perfil e a sua escolha
                        if editarPerfilCliente == '1':
                            print('='*30 + '# ATUALIZAR NOME DE USUÁRIO #' + '='*30)
                            print(f'Seu nome de usuário atual é {nomeUser}.')                            
                            novoNomeUserCliente = input('Insira seu novo nome de usuário: ')
                            if novoNomeUserCliente.isdigit(): # verifica se é um nome alfabético
                                print('Por favor, utilize apenas carateres alfabéticos.')
                            else:
                                nomeUser = novoNomeUserCliente
                                print(('#'*30) +'\n NOME DE USUÁRIO ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                break
                            
                        elif editarPerfilCliente == '2':
                            print('='*30 + '# TROCAR SENHA #' + '='*30)
                            print('-'*15 + '| FAÇA LOGIN PARA CONTINUAR |' + '-'*15)
                            functCleintes.trocarSenhaCliente(email, clientes)

                        elif editarPerfilCliente == '0':
                            break

                        else:
                            print('Opção inválida.')

                elif opcaoMenuCliente == '0':
                    print('Retornando ao menu principal.')
                    break

                else:
                    print('Opção inválida.')
                    continue
    
        elif email in admins: #verificar se o usuário é um ADM que quer acessar a aba de clientes
            print("ADM's não podem comprar ingressos.")

        else:
            print('Email ou senha inválidos.') #imprimir mensagem que não deixa explícito qual dado inserido está correto.
                        
    elif opcaoMenuPrincipal == '3':
        functAdmins.cadastrarUsuario(admins, clientes)

    elif opcaoMenuPrincipal == '0':
        print('Finalizando programa.')
        break

    else:
        print('Opção inválida.')
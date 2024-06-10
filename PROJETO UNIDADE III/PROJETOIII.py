import os
import enviarEmail
import functCleintes

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
                    print('='*30 + '# CADASTRAR FILME #' + '='*30)
                    if infosSala1[1] or infosSala2[1] or infosSala3[1]:
                        nomeFilmeCadastro = input('Digite o nome do filme que deseja cadastrar: ').upper() # [0]
                        while True:
                            duracaoFilme = input('Insira a duração do filme em minutos: ') # [1]
                            if duracaoFilme[0] == '-':
                                print('Por favor, insira um valor positivo.')
                                continue
                            else:
                                break
                        while True:
                            salaDoFilme = input('Insira a sala na qual deseja disponibilizar o filme [1 - 2 - 3]: ') # [2]
                            if salaDoFilme == '1':
                                
                                if infosSala1[1]:
                                    filmeOcupante = nomeFilmeCadastro # infosSala1[0]
                                    statusSala1 = ocupado # infosSala1[1]
                                    infosSala1[0] = filmeOcupante
                                    infosSala1[1] = statusSala1
                                    break
                                else:
                                    print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                            elif salaDoFilme == '2':
                                
                                if infosSala2[1]:
                                    filmeOcupante = nomeFilmeCadastro # infosSala2[0]
                                    statusSala2 = ocupado # infosSala2[1]
                                    infosSala2[0] = filmeOcupante
                                    infosSala2[1] = statusSala2
                                    break
                                else:
                                    print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                            elif salaDoFilme == '3':
                                
                                if infosSala3[1]:
                                    filmeOcupante = nomeFilmeCadastro # infosSala3[0]
                                    statusSala3 = ocupado # infosSala3[1]
                                    infosSala3[0] = filmeOcupante
                                    infosSala3[1] = statusSala3
                                    break
                                else:
                                    print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                            else:
                                print('Por favor, insira uma sala válida.')
                                continue
                        while True:
                            capacidadeFilme = int(input('Digite a quantidade de ingressos disponíveis para o filme: ')) # [3]
                            if capacidadeFilme > 0:
                                capacidadeFilmeVerificacao = capacidadeFilme # [7] armazena a sempre a capacidade mais atualizada do filme
                                break
                            elif capacidadeFilme == 0:
                                print('A capacidade do filme não pode ser 0.')
                            else:
                                print('Por favor, insira um valor positivo.')
                                continue
                        horarioFilme = input('Insira o horário no qual o filme irá passar: ') # [4]
                        while True:
                            precoIngresso = float(input('Digite o valor do ingresso a ser cobrado para esse filme: ')) # [5]
                            if precoIngresso < 0:
                                print('Por favor, insira um valor positivo.')
                                continue
                            elif precoIngresso == 0:
                                print('Não é possível fornecer ingressos gratuitos.')
                                continue
                            else:
                                break                            
                        autorFilme = input('Insira o autor do filme: ') # [6]                        
                        filmes.append([nomeFilmeCadastro, duracaoFilme, salaDoFilme, capacidadeFilme, horarioFilme, precoIngresso, autorFilme, capacidadeFilmeVerificacao])
                        print(('#'*30) +'\nFILME CADASTRADO\n'+ ('#'*30))
                    else:
                        print('TODAS AS SALAS ESTÃO OCUPADAS.\nREMOVA UM FILME PARA REALIZAR MAIS UM CADASTRO.')
                elif opcaoMenuADM == '2':
                    while True: # while menu busca de filmes
                        naoRemovido = True
                        print('='*30 + '# BUSCAR FILMES #' + '='*30)
                        buscaFilme = input('Digite o nome do Filme que deseja buscar ou 0 para voltar ao menu anterior: ').upper()
                        if buscaFilme == '0':
                            break
                        elif len(filmes) == 0:
                            print('Não há nenhum filme cadastrado.')
                        for filme in filmes: # busca cada lista nas listas de filme
                            if buscaFilme == filme[0]: # compara o nome buscado com o nome da lista (indice 0 corresponde ao nome)
                                filmeEncontradoADM = True
                                print('Filme encontrado.')
                              
                                                               
                        if filmeEncontradoADM:
                            while naoRemovido:
                                opcaoMenuBuscaFilme = input(f'O que deseja fazer com o filme {buscaFilme}?\n[1] Atualizar o filme {buscaFilme}\n[2] Remover o filme {buscaFilme}\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
                                if opcaoMenuBuscaFilme == '1':
                                    while True:
                                        print('='*30 + '# ATUALIZAR FILME #' + '='*30)
                                        print(f'Filme: {filme[0]}', f'| Duração: {filme[1]} min', f'| Sala: {filme[2]}', f'| Ingressos disponíveis: {filme[3]}', f'| Horário: {filme[4]}', f'| Preço: R${filme[5]}', f'| Autor: {filme[6]}', end=' | \n')
                                        opcaoMenuAtualizarFilme = input(f'O que deseja atualizar no filme {buscaFilme}?\n[1] Nome do filme\n[2] Duração do filme\n[3] Sala do filme\n[4] Capacidade de espectadores\n[5] Horário do Filme\n[6] Preço do ingresso\n[7] Autor do filme\n[0] Voltar ao menu anterior\nEscolha sua opção: ' )
                                        if opcaoMenuAtualizarFilme == '1':
                                            novoNomeFilme = input('Insira o novo nome do filme: ').upper()
                                            filme[0] = novoNomeFilme
                                            print(('#'*30) +'\nNOME ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                        elif opcaoMenuAtualizarFilme == '2':
                                            while True:
                                                novaDuracao = input('Insira a nova duração do filme: ')
                                                if novaDuracao[0] == '-':
                                                    print('Por favor, insira um valor positivo.')
                                                    continue
                                                else:
                                                    filme[1] = novaDuracao
                                                    print(('#'*30) +'\nDURAÇÃO ATUALIZADA COM SUCESSOO\n'+ ('#'*30))
                                                    break
                                        elif opcaoMenuAtualizarFilme == '3':
                                            while True:
                                                salaAntiga = input('Insira a sala antiga do filme: ')                                                   
                                                if salaAntiga == '1':
                                                    while True:
                                                        novaSala = input('Insira a nova sala do filme [2 - 3]: ')                                         
                                                        if novaSala == '2':
                                                            if infosSala2[1]:
                                                                filme[2] = novaSala
                                                                infosSala2[1] = ocupado
                                                                infosSala1[1] = livre
                                                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                                                break
                                                            else:
                                                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                                                        elif novaSala == '3':
                                                            if infosSala3[1]:
                                                                filme[2] = novaSala
                                                                infosSala3[1] = ocupado
                                                                infosSala1[1] = livre
                                                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                                                break
                                                            else:
                                                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                                                        else:
                                                            print('Por favor, insira uma sala válida.')
                                                            continue
                                                        break
                                                elif salaAntiga == '2':
                                                    while True:
                                                        novaSala = input('Insira a nova sala do filme [1 - 3]: ')
                                                        if novaSala == '1':
                                                            if infosSala1[1]: # livre = True | ocupado = False
                                                                filme[2] = novaSala
                                                                infosSala1[1] = ocupado
                                                                infosSala2[1] = livre
                                                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                                                break
                                                            else:
                                                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')
                                                        elif novaSala == '3':
                                                            if infosSala3[1]:
                                                                filme[2] = novaSala
                                                                infosSala3[1] = ocupado
                                                                infosSala2[1] = livre
                                                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                                                break
                                                            else:
                                                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                                                        else:
                                                            print('Por favor, insira uma sala válida.')
                                                            continue
                                                        break
                                                elif salaAntiga == '3':
                                                    while True:
                                                        novaSala = input('Insira a nova sala do filme [1 - 2]: ')
                                                        if novaSala == '1':
                                                            if infosSala1[1]: # livre = True | ocupado = False
                                                                filme[2] = novaSala
                                                                infosSala1[1] = ocupado
                                                                infosSala3[1] = livre
                                                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                                                break
                                                            else:
                                                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')
                                                        elif novaSala == '2':
                                                            if infosSala2[1]:
                                                                filme[2] = novaSala
                                                                infosSala2[1] = ocupado
                                                                infosSala3[1] = livre
                                                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                                                break
                                                            else:
                                                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                                                        else:
                                                            print('Por favor, insira uma sala válida.')
                                                            continue
                                                        break
                                                else:
                                                    print('Por favor, insira uma sala válida.')
                                                                                            
                                        elif opcaoMenuAtualizarFilme == '4':
                                            while True:
                                                novaCapacidade = int(input('Insira a nova capacidade do filme: '))
                                                if novaCapacidade > 0:
                                                    filme[7] = novaCapacidade # armazena sempre a capacidade mais atualizada do filme
                                                    novaCapacidade -= qtdIngressosCompra # retira a quantidade de ingressos já comprados
                                                    filme[3] = novaCapacidade
                                                    print(('#'*30) +'\nCAPACIDADE ATUALIZADA COM SUCESSO\n'+ ('#'*30)) 
                                                    break
                                                elif novaCapacidade == 0:
                                                    print('A capacidade do filme não pode ser 0.')
                                                else:
                                                    print('Por favor, insira um valor positivo.')
                                                    continue
                                            
                                        elif opcaoMenuAtualizarFilme == '5':
                                            novoHorario = input('Insira o novo horário do filme: ')                                
                                            filme[4] = novoHorario
                                            print(('#'*30) +'\nHORÁRIO ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                        elif opcaoMenuAtualizarFilme == '6':
                                            while True:
                                                novoPreco = float(input('Insira o novo preço do filme: '))
                                                if novoPreco < 0:
                                                    print('Por favor, insira um valor positivo.')
                                                    continue
                                                elif novoPreco == 0:
                                                    print('Não é possível fornecer ingressos gratuitos.')
                                                    continue
                                                else:
                                                    filme[5] = novoPreco
                                                    print(('#'*30) +'\nPREÇO ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                                    break                                           
                                        elif opcaoMenuAtualizarFilme == '7':
                                            novoAutor = input('Insira o novo autor do filme: ')
                                            filme[6] = novoAutor
                                            print(('#'*30) +'\nAUTOR ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                        elif opcaoMenuAtualizarFilme == '0':
                                            break
                                        else:
                                            print('Opção inválida.')

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
                    print('='*30 + '# BUSCAR CLIENTE #' + '='*30)
                    emailBuscaCliente = input('Insira o email do cliente que deseja buscar: ')
                    if len(clientes) == 0:
                        print('Nenhum cliente cadastrado.')
                    else:
                        for cliente in clientes:
                            if emailBuscaCliente == cliente:
                                print('Cliente encontrado.')
                                clienteEncontrado = True # controle do if que roda a busca do cliente
                            
                    if clienteEncontrado:
                        while True:
                            opcaoMenuBuscaCliente = input(f'O que deseja fazer com o cliente {emailBuscaCliente}?\n[1] Atualizar dados do cliente\n[2] Remover o cliente\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
                            if opcaoMenuBuscaCliente == '1':
                                while True:
                                    print('='*30 + '# ATUALIZAR CLIENTE #' + '='*30)
                                    opcaoMenuAtualizarCliente = input(f'Qual dado do cliente deseja atualizar?\n[1] Email\n[2] Senha\n[0] Voltar ao menu anterior \nEscolha sua opção: ' )
                                    if opcaoMenuAtualizarCliente == '1':
                                        novoEmail = input('Insira o novo email do cliente: ')
                                        clientes[novoEmail] = clientes[emailBuscaCliente] # salva as informações do antigo no novo
                                        del clientes[emailBuscaCliente] # e deleta ele
                                        emailBuscaCliente = novoEmail
                                        print(('#'*30) +'\nEMAIL ATUALIZADO COM SUCESSO\n'+ ('#'*30))
                                        break
                                    elif opcaoMenuAtualizarCliente == '2':
                                        novaSenha = input('Insira a nova senha do cliente: ')
                                        clientes[emailBuscaCliente] = novaSenha
                                        print(('#'*30) +'\nSENHA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                        break
                                    
                                    elif opcaoMenuAtualizarCliente == '0':
                                        break
                                
                                    else:
                                        print('Opção inválida.')
                                        continue
                                    
                            elif opcaoMenuBuscaCliente == '2':
                                while True:
                                    print('='*30 + '# REMOVER CLIENTE #' + '='*30)
                                    certeza = input(f'Tem certeza que deseja remover o cliente {emailBuscaCliente}?\n(s/n): ').lower()
                                    if certeza == 's':
                                        del clientes[emailBuscaCliente]
                                        print(('#'*30) +'\nCLIENTE REMOVIDO COM SUCESSO\n'+ ('#'*30))
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
                        opcaoOutrasOpcoes = input('[1] Atualizar nome de usuário\n[2] Trocar senha de admin\n[3] Atualizar email\n[0] Voltar ao menu anterior\nEscolha uma opção: ')
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
                                carrinhoCliente = [] # cria o carrinho proprio do cliente
                                while True:
                                    qtdIngressosCompra = int(input(f'Insira a quantidade e ingressos que deseja para o filme {filmeCompra}: '))
                                    if qtdIngressosCompra <= filmeQueFoiEncontrado[3]: # verifica se o cliente escolheu uma quantidade <= aos ingressos restantes para o filme
                                        filmeQueFoiEncontrado[3] -= qtdIngressosCompra
                                        valorIngressoCompradoCliente = filmeQueFoiEncontrado[5] * qtdIngressosCompra
                                        carrinhoCliente.append(filmeQueFoiEncontrado[0]) # [0]
                                        carrinhoCliente.append(valorIngressoCompradoCliente) # [1]
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
                                                functCleintes.lancheCarrinho(precoLanche, lanche, email, carrinhoCliente, carrinhos)
                                                break
                                            elif menuLanches == '2':
                                                precoLanche = 11.99
                                                lanche = 'Hambúrguer + Refri GPFresco'
                                                functCleintes.lancheCarrinho(precoLanche, lanche, email, carrinhoCliente, carrinhos)
                                                break
                                            elif menuLanches == '3':
                                                precoLanche = 14.99
                                                lanche = 'Combo Pipoca + MilkShake'
                                                functCleintes.lancheCarrinho(precoLanche, lanche, email, carrinhoCliente, carrinhos)
                                                break
                                    
                                        elif escolhaComida in escolhasNegativas:
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
                                    print('-' * 65 + f'\nFilme escolhido: {carrinhos[cliente][0]} | Valor do(s) ingresso(s): R$ {carrinhos[cliente][1]}\nLanche: {carrinhos[cliente][3]} | Preço do lanche: R$ {carrinhos[cliente][2]}\n' + '-' * 65 + f'\nPreço total: R$ {(carrinhos[cliente][1] + carrinhos[cliente][2]):.2f}')
                                    precoTotalComLanche = (carrinhos[cliente][1] + carrinhos[cliente][2])
                                    comLanche = True

                                else: # se não, só o filme
                                    print('-' * 65 + f'\nFilme escolhido: {carrinhos[cliente][0]} | Valor do(s) ingresso(s): R$ {carrinhos[cliente][1]:.2f}\n' + '-' * 65 + f'\nPreço total: R$ {carrinhos[cliente][1]:.2f}')
                                    precoTotalSemLanche = carrinhos[cliente][1]
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

                            enviarEmail.enviar_email(precoTotalPrint, pagouNo, desconto, acrescimo, valorPagamento)
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
        print('='*30 + '# CADASTRAR USUÁRIO #' + '='*30)
        while True: #while menu de cadastro
            contadordeArroba = 0
            contadordePonto = 0
            
            email = input('Insira o email que deseja cadastrar: ').lower()
            if ('@' in email) and ('.com' in email):
                for caractere in email:
                    if caractere == '@':
                        contadordeArroba += 1
                    if caractere == '.':
                        contadordePonto += 1

                if (contadordeArroba == 1) and (contadordePonto == 1):
                    break
            else:
                print('Por favor, insira um email válido.\nEx: email@dominiodoemail.com')
                continue
        while True: # while confirmar senha
            senhaUm = input('Insira sua senha: ')
            senhaConfirmacao = input('Insira sua senha novamente para confirmar: ')
            if senhaConfirmacao == senhaUm:
                senha = senhaConfirmacao
                break
            else:
                print('As senhas estão diferentes.')
                continue
        if (email in admins) or (email in clientes): # verifica se o usuário não já está cadastrado
            print(('#'*30) +'\nUSUÁRIO JÁ CADASTRADO\n'+ ('#'*30))
        else:
            while True: # while tipo de cadastro
                opcaoCadastro = input('Selecione o tipo de conta que deseja cadastrar.\n[1] ADM\n[2] Cliente\nEscolha uma opção: ')
                if opcaoCadastro == '1':
                    admins[email] = (senha)
                    print(('#'*30) +'\nADM CADASTRADO\n'+ ('#'*30))
                    break
                elif opcaoCadastro == '2':
                    clientes[email] = (senha)
                    print(('#'*30) +'\nCLIENTE CADASTRADO\n'+ ('#'*30))
                    break
                else:
                    print('Opção inválida.')
                    continue

    elif opcaoMenuPrincipal == '0':
        print('Finalizando programa.')
        break

    else:
        print('Opção inválida.')
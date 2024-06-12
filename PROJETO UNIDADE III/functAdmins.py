def funcCadastrarFilme(infosSala1, infosSala2, infosSala3, ocupado, filmes):
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

def funcAtualizarFilme(buscaFilme, infosSala1, infosSala2, infosSala3, livre, ocupado, qtdIngressosCompra, filme):
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
            salaNaoAlterada = True
            while salaNaoAlterada:
                salaAntiga = input('Insira a sala antiga do filme: ')                                                   
                if salaAntiga == '1':
                    while True:
                        novaSala = input('Insira a nova sala do filme [2 - 3]: ')                                         
                        if novaSala == '2':
                            if infosSala2[1]:
                                filme[2] = novaSala
                                infosSala2[1] = ocupado
                                infosSala1[1] = livre
                                salaNaoAlterada = False
                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                break
                            else:
                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')

                        elif novaSala == '3':
                            if infosSala3[1]:
                                filme[2] = novaSala
                                infosSala3[1] = ocupado
                                infosSala1[1] = livre
                                salaNaoAlterada = False
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
                                salaNaoAlterada = False
                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                break
                            else:
                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')
                        elif novaSala == '3':
                            if infosSala3[1]:
                                filme[2] = novaSala
                                infosSala3[1] = ocupado
                                infosSala2[1] = livre
                                salaNaoAlterada = False
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
                                salaNaoAlterada = False
                                print(('#'*30) +'\nSALA ATUALIZADA COM SUCESSO\n'+ ('#'*30))
                                break
                            else:
                                print('SALA OCUPADA.\nPOR FAVOR, ESCOLHA OUTRA SALA.')
                        elif novaSala == '2':
                            if infosSala2[1]:
                                filme[2] = novaSala
                                infosSala2[1] = ocupado
                                infosSala3[1] = livre
                                salaNaoAlterada = False
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

def funcAtualizarDadosCliente(emailBuscaCliente, clientes):
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

def cadastrarUsuario(admins, clientes):
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
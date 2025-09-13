import os

restaurantes =[{'nome':'McDonalds', 'categoria':'Fast Food','ativo':True},
               {'nome':'Fratelli', 'categoria':'Italiana','ativo':False}]
      

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    
    print(""""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ """)

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''    

    print('1.Cadatrar restaurante')

    print('2.Listar restaurantes')

    print('3.Altermar status do restaurante')

    print ('4.Sair \n')

def finalizar_app():  #funcao que define a finalização do app
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    input('\nDigite uma tecla para voltar ao menu')
    main()


def opcao_invalida():
    print('Opção inválida! \n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
'''

def cadastrar_novo_restaurante():
    '''FUNCAO RESPONSAVEL POR CADASTRAR NOVOS RESTAURANTES
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:

    - Adciona uma nome restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastrode novos restaurantes')
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a catergoria do restaurante:{nome_do_restaurante}:')
    
    #DICIONARIO DE DADOS
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}

    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''


    exibir_subtitulo('Listando os restaurantes')
    print(f' {'Nome do restaurante'.ljust(22)} |{'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')


    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurate_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem =(f'O restaurante {nome_restaurante} for ativado com sucesso!'
            if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!')
            print(mensagem)
    if not restaurante_encontrado:
        print ('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''


    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) #converte string do input em integer pra funcionar nos condicionais

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante() 
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
        os.system('clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()
import os

restaurantes = [{'nome':'Hakkoi','categoria':'japonesa','ativo':False}, 
                {'nome': 'Pizza suprema', 'categoria': 'italiana', 'ativo': True},
                {'nome': 'Feijoada Vava', 'categoria': 'brasileira', 'ativo': False},
                {'nome': 'Didi lanches', 'categoria': 'sobremesa', 'ativo': False},
                {'nome': 'Acaiteria Gourmet', 'categoria': 'sobremesa', 'ativo': True},
                {'nome': 'Cafe com Deus pai', 'categoria': 'cafeteria', 'ativo': True}]


def exibir_o_nome_do_programa():
    '''Essa funcao é responsável por exibir o nome do programa'''  
    os.system('cls')
    print(' ')
    print('Ｃａｎｔｉｎａ Ｍｏｉｎｈｏ🥐☕\n')

def exibir_opcoes():
    '''Essa funcao é responsável por exibir as opções do menu'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa funcao é responsável por finalizar o app'''
    exibir_subtitulos('Finalizando o app\n')

def opcao_invalida():
    '''Essa funcao é responsável por retornar que a opcao escolhida é inválida
    
    Outputs:
    -Mensagem de erro
    -Voltar ao menu principal
    
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulos(texto):
    '''Essa funcao é responsavel por exibir subtítulos
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa funcao é responsavel por cadastrar um novo restaurante

    Inputs:
    -Nome do restaurante
    -Categorias
    
    Output:
    -Lista de restaurantes

    '''
    exibir_subtitulos('Cadastrar novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante: {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante,
    'categoria': categoria, 'ativo': False} #regra de negocio, sempre False
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()
    
def voltar_ao_menu_principal():
    '''Essa funcao é responsavel por voltar ao menu principal'''
    input('Digite uma tecla para voltar ao menu:  ')
    input(main())

def listar_restaurantes():
    '''Essa funcao é responsavel por listar todos os restaurantes
    
    Output:
    -Lista de restaurantes
    '''
    exibir_subtitulos('Listar restaurantes\n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
          
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' #o que é verdadeiro, se essa condicao é verdadeira e se não é | condicional em uma linha
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
              
    voltar_ao_menu_principal()
    

def ativar_restaurante():
    '''Essa funcao é responsavel por ativar os restaurantes'''
    os.system('cls')
    print('Ativar restaurante\n')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa funcao é responsavel por alternar o estado dos restaurantes
    
    Output:
    -Indica mudança de estado do restaurante
    '''
    exibir_subtitulos('Alternar estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #alternar ativo p inativo visse versa
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            

    if not restaurante_encontrado:
        '''Esta funcao é responsavel por retornar que o restaurante não foi encontrado'''
        print(f'Restaurante {nome_restaurante} não encontrado!')


    voltar_ao_menu_principal()

def escolher_opcao():
    '''Esta funcao é responsavel por escolher a opcao do menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

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
    except ValueError:
        opcao_invalida()


def main():
    '''Esta funcao é responsavel por chamar as outras funcoes'''
    exibir_o_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    os.system('cls')


if __name__ == '__main__':
    main()
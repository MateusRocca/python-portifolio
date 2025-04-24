import os

restaurantes = [{'nome': 'Monster Burguer', 'categoria': 'Hamburguer', 'ativo': False}, 
                {'nome': 'Koma Bem', 'categoria': 'Pizzaria', 'ativo': True},
                {'nome': 'Inês Salgados', 'categoria': 'Salgados', 'ativo': False}
                ]


def voltar_ao_menu_principal():
    print()
    input('Digite uma tecla para voltar para o menu principal!\n')
    main()  

def exibe_subtitulo(titulo):
    os.system('cls')
    linha = '*' * len(titulo)
    print(linha)
    print(titulo)
    print(linha)
    print()

def exibir_nome_empresa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair')
    print()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()
    

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('\nInforme a opção desejada: '))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
   
def finalizar_app():
    exibe_subtitulo('Finalizando o APP')


def cadastrar_restaurante():
    exibe_subtitulo('Cadastro de restaurantes!')
    nome_do_restaurante = input('Insira o nome do novo restaurante: ')
    categoria = input(f'Insira a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibe_subtitulo('Listando os restaurantes...')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'» {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibe_subtitulo('Alterar estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com suceeso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    
    voltar_ao_menu_principal()



def main():
    os.system('cls')
    exibir_nome_empresa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
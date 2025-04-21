import os

restaurantes = ['Monster Burguer', 'Dona Pizza', 'Kebab']
def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar para o menu principal!\n')
    main()  

def exibe_subtitulo(titulo):
    os.system('cls')
    print(titulo)
    print()

def exibir_nome_empresa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()
    

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Informe a opção desejada:'))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativando restaurante')
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
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibe_subtitulo('Listando os restaurantes...')
    for restaurante in restaurantes:
        print(f'» {restaurante}')
    voltar_ao_menu_principal()

def main():
    os.system('cls')
    exibir_nome_empresa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
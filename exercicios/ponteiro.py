def referencia(nova_lista):
    nova_lista[1] = 'novo valor'

def ponteiro():
    lista = []
    print(f'Tamanho da lista {len(lista)}')

    lista = ['O carro', 'peixe', 123, 111]

    for elemento in lista:
        print(f'Original {elemento}')

    referencia(lista)
    print('-------')

    for elemento in lista:
        print(f'Teste {elemento}')

ponteiro()
def conjunto_imutavel():
    lista_um = ['Maça', 'Banana', 'Morango']
    print(f'Exemplo lista um: {lista_um}')

    conjunto_congelado_um = frozenset(lista_um)
    print(f'Exemplo com conjunto um: {conjunto_congelado_um}')

    conjunto_dois = {'Gui', 34, True, 40, 'masculino'}
    print(f'Conjunto dois: {conjunto_dois}')

    conjunto_congelado_dois = frozenset(conjunto_dois)
    print(f'Exemplo com conjunto dois: {conjunto_congelado_dois}')

    contador = 1
    for extracao in conjunto_congelado_dois:
        print(f'Extraindo elemento: {contador} - {extracao}')
        contador += 1
    

conjunto_imutavel()

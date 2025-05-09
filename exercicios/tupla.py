def tupla_inicio():
    primeira_tupla = (1, 3, 'Teste', 0.4)
    print(f'Primeira tupla: {primeira_tupla}')

    segunda_tupla = 3, 6, 9
    print(f'Segunda tupla: {segunda_tupla}')

    print(f'Tamanho da tupla:  {len(primeira_tupla)}')

    primeira_tupla += 'Novo elemento',
    print(f'Acrescenta um novo elemento a tupla: {primeira_tupla}')

    print(f'Tipo de dados: {type(primeira_tupla)}')
    print(f'Referência ao elemento 3: {primeira_tupla[2]}')

    primeira_tupla += (4,8,9)
    print(primeira_tupla)

    primeira_tupla = primeira_tupla * 6
    print(primeira_tupla)

tupla_inicio()
def conjunto():
    primeiro_set = {6, 'Dez', 4}
    print(f'Conjunto: {primeiro_set}')

    primeiro_set.add('Um')
    print(f'Adicionando um elemento ao conjunto: {primeiro_set}')

    primeiro_set.remove('Dez')
    print(f'Exemplo do set com "Remove": {primeiro_set}')

    primeiro_set.discard('Dez')
    print(f'Exemplo do set com "Discard": {primeiro_set}')

    print(f'Tamanho do conjunto: {len(primeiro_set)}')

    segundo_set = {3,2,4, True, 'Novo', 20, 5, 'Um'}
    print(f'Segundo set: {segundo_set}')

    uniao = primeiro_set.union(segundo_set)
    print(f'União: {uniao}')

    intersecao = primeiro_set.intersection(segundo_set)
    print(f'Interseção: {intersecao}')

conjunto()
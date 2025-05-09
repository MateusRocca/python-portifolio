import datetime

def dicionario():
    dicionario = {'Nome': 'Mateus', 'Idade': 32, 'Maior idade': True, 'Sálario': 1921.12, 
                  'Filhos':[{'Nome': 'Gu', 'Idade': 3}, {'Nome': 'Jô', 'Idade': 14}],
                  'Números primos': [1,2,3,5,7]}
    print(f'Dicionário: {dicionario} \n')

    print(f'Exibir a informação da idade: {dicionario["Idade"]} \n')
    print(f'Teste do get: {dicionario.get("caso", 0)} \n')
    print(f'Retorna uma tupla: (chave, valor): {dicionario.items()} \n')
    print(f'Retorna somente chaves: {dicionario.keys()} \n')
    print(f'Retorna somente os valores: {dicionario.values()} \n')

    dicionario.update({'dataNascimento': datetime.datetime(1980, 2, 20)})
    print(f'Imprimindo os dados do dicionário')
    for chave, valor in dicionario.items():
        if chave == 'dataNascimento':
            print('Exibindo os dados da chave: ', chave, 'com o valor ', valor.strftime("%d/%m/%Y"))
        elif chave == 'filhos':
            for i in range(len(valor)):
                for chaveFilhos, valorFilhos in valor[i].items():
                    print('Exibindo os itens da chave filhos: ', chaveFilhos, 'com o valor dos filhos ', valorFilhos)
        elif chave == 'Números primos':
            for i in range(len(valor)):
                print('Valor primos ', valor[i])
        else:
            print('Exibindo os dados da chave ', chave, 'com o valor ', valor)


dicionario()
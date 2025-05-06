print('Definição de vetores.')
print()

def main():
    vetor_vazio = []

    #imprime o tamanho do vetor
    print(f'Tamanho do vetor vazio é {len(vetor_vazio)}')
    for i in range(9): #for(i = 0, i<9, i++)
        #acrescenta um valor ao final do vetor
        vetor_vazio.append(i)
    
    print(f'Novo tamanho do vetor vazio é: {len(vetor_vazio)}')
    print(f'Valores agora no vetor vazio são: {vetor_vazio}')

    vetor_inteiros = [1,2,3,4,5,6,7]

    #imprime [1,2,3,4,5,6,7]
    print(f'Valor do vetor inteiros são: {vetor_inteiros}')

    for i in range(0, len(vetor_inteiros)):
        print(f'O valor na posição {i} é: {vetor_inteiros[i]}')

    vetor_caracteres = ['Maria', 'Mateus', 'Gustavo', 'Marcela', 'Rubens']

    for i in range (len(vetor_caracteres)):
        print(f'O valor na posição {i} é: {vetor_caracteres[i]}')

    vetores_reais = [1.2, 3.5, 2.6, 12.5]
    print(f'Valores nos vetores reais são: {vetores_reais}')

main()
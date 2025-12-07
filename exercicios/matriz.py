def bidimensional():
    bidimensional = [
        [1,2,3,4], 
        [9,8,7,6]
        ]
    print(len(bidimensional))

    for i in range (0, len(bidimensional)): #primeiro for percorre a linha
        #neste for é acessado o primeiro nível da matriz
        for j in range (0, len(bidimensional[i])): #segundo for percorre a coluna
            #neste for é acessado o segundo nível, onde contém os dados
            print('Bidimensional valor [',i,',',j,']', bidimensional[i][j])


def tridimensional():
    tridimensional = [
        [[1,2,3,4], [4,3,2,1]], 
        [[9,8,7,6,], [4,5,6,7]]
        ]
    print(len(tridimensional)) #contém 2 itens

    for i in range (0, len(tridimensional)): #camada. for será executado 2 vezes 0 e 1
        #neste for é acessado o primeiro nível da matriz
        for j in range (0, len(tridimensional[i])): #linha de cada camada
            #neste for é acessado o segundo nível da matriz
            for k in range (0, len(tridimensional[i][j])): #coluna de cada camada
                #neste for é acessado o segundo nível, onde contém os dados
                print("Tridimensional Valor [", i, ",", j, ",", k, "]: ", tridimensional[i][j][k])

                '''
                i = Qual andar (camada)

                j = Qual gaveta (linha)

                k = Qual item dentro da gaveta (coluna)
                '''

def executar_aplicacao():
    print('Exemplo de Matriz (Vetor Bidimensional)')
    bidimensional()
    print('-----------------------------\n\n')

    print('Exemplo de Matriz de três dimensões (Vetor Tridimensional)')
    tridimensional()
    print('-----------------------------\n\n')

executar_aplicacao()
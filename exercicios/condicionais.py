'''
    EXERCÍCOS USANDO CONDICIONAIS IF, ELSE, ELIF

    Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas 
    no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
    Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

    Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem 
    indicando qual deles vendeu mais. Se as quantidades forem iguais, 
    exiba uma mensagem dizendo que houve empate.    
'''

banana = int(input('Insira a quantidade de bananas que foram vendidas: '))

maca = int(input('Insira a quantidade de macas que foram vendidas: '))

if banana > maca:
    print(f'Banana vendeu mais! Banana vendeu {banana} quantidades.')
elif banana < maca:
    print(f'Maçã vendeu mais que banana! Maçã vendeu {maca} quantidades.')
else:
    print('Banana e Maçã tiveram a mesma quantidade de vendas!')
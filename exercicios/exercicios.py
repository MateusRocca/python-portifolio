'''1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.'''

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Mateus', 'Fernando', 'Galdino', 'Rocca']
anos = ['1993', '2025']

'''2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.'''
#for numero in numeros:
#    print(numero)

'''3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

'''

'''4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
numeros = 0
for i in range(10, 0, -1):
    print(i)
'''

'''5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input('Insira o número: \n'))
print(f'Tabuada de {numero}')
for i in range(0, 11, 1):
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')
'''

'''6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
Utilize um bloco try-except para lidar com possíveis exceções.
numeros = [1,2,3,4,5,6,7,8,9]
soma = 0
try:
    for numero in numeros:
        soma += numero
    print(soma) 
except:
    print('A lista contém elementos inválidos')
'''


'''7 - Construa um código que calcule a média dos valores em uma lista. 
Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

'''

lista = [1,5,2,4]
soma = 0
media = 0
lista_tamanho = len(lista)
try:
    for i in lista:
        soma += i
    media = soma / lista_tamanho
    print(media)
    lista_valores = [15, 20, 25, 30]
    soma_valores = 0
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

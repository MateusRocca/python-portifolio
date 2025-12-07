'''
    EXERCÍCOS USANDO CONDICIONAIS IF, ELSE, ELIF
    Índice de Massa Corporal (IMC)  
    O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, 
    além de indicar se está abaixo do peso, com peso normal ou acima do peso. 
    Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: 
    IMC = peso / (altura ** 2) 
    Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), 
    peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
'''

peso = float(input('Insira o seu peso (kg): '))
altura = float(input('Insira a sua altura (m): '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está com peso normal!')
else:
    print('Você está acima do peso!')
'''
    EXERCÍCOS USANDO CONDICIONAIS IF, ELSE, ELIF
    Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir 
    três atividades: A, B e C. 
    No entanto, se alguma atividade tiver um número de dias negativo, 
    o código deve avisar que os valores inseridos são inválidos e não calcular o total.

    Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
    Se algum valor for negativo, mostre uma mensagem informando o erro.
'''

atividade_a = int(input('Informe os dias para a atividade A: '))
atividade_b = int(input('Informe os dias para a atividade B: '))
atividade_c = int(input('Informe os dias para a atividade C: '))


if atividade_a  < 0 or atividade_b < 0 or atividade_c < 0:
    print('Erro: Os dias não podem ser negativos!')
else:
    total = atividade_a + atividade_b + atividade_c
    print(f'Total de dias para realizar as atividades A, B e C: {total}')
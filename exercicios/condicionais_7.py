'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos
e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final.
Com base na média, exiba a situação do aluno.

'''

nota_1 = float(input('Informe a nota 1: '))
nota_2 = float(input('Informe a nota 2: '))
nota_3 = float(input('Informe a nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print('Aprovado!')
elif 5 <= media < 7:
    print('Recuperação!')
else:
    print('Reprovado!')

notas = []

while True:
    try:
        nota = float(input('Informe a nota ou digite -1 para sair: '))
        if nota == -1:
            break
        notas.append(nota)
    except ValueError:
        print('Valor inválido. Por favor, digite um número.')

print('Notas informadas:', notas)

if len(notas) > 0: #evita divisão por 0 se nenhuma nota for inserida
    total = sum(notas)
    media = total / len(notas)  # Calcula média só depois da soma completa
    print(f'Média: {media:.2f}')

    if media >= 7:
        print('Aprovado!')
    elif 5 <= media < 7:
        print('Recuperação!')
    else:
        print('Reprovado!')
else:
    print('Nenhuma nota informada.')

__________________________________________________

nota_1 = float(input('Informe a nota 1: '))
nota_2 = float(input('Informe a nota 2: '))
nota_3 = float(input('Informe a nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3
print(f'Média: {media:.2f}')

# Avaliação direta
print('Aprovado!' if media >= 7 else 'Recuperação!' if 5 <= media < 7 else 'Reprovado!')

_________________________________________



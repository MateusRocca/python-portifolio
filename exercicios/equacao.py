#EQUAÇÃO DE 2° GRAU

def delta(a, b, c):
    return (b ** 2 - 4 * a * c)

def equacao(a, b, c):
    resultado_delta = delta(a, b, c)
    if resultado_delta < 0:
        return 'Não possuí resultados reais.'
    else:
        print(f'Delta {resultado_delta}')

    x1 = (((-1) * b) + (resultado_delta ** (1/2))) / (2 * a)
    x2 = (((-1) * b) - (resultado_delta ** (1/2))) / (2 * a)

    return f'Os resultados possíveis são:  \n X1: {x1:.2f} \n X2: {x2:.2f}'

def main():
    print('Cálculo de equação do 2° grau \n ax²+bx+c=0')
    print('\n')

    try:
        valorA = int(input('Informe o valor de "a": '))
        valorB = int(input('Informe o valor de "b": '))
        valorC = int(input('Informe o valor de "c": '))

        print(equacao(valorA, valorB, valorC))
    except ValueError as erro:
        print('O valor informado não é inteiro!')

main()
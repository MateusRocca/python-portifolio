'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar
suas despesas. O programa deve receber o total de despesas realizadas 
e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
'''

limite = 3000
despesas = float(input('Informe o valor total das despesas: '))

if despesas > limite:
    saldo_devedor = despesas - limite
    print(f'Você ultrapassou o limite estabelecido. Limite de {limite} e seus gastos foram de {despesas:.2f}. Você ultrapassou {saldo_devedor:.2f} do limite!')
else:
    sobra = limite - despesas
    print(f'Você está dentro do limite. Você ainda tem {sobra:.2f} para gastar!')
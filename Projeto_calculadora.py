# Calcularora básica

num1 = float(input('Digite um número: '))

print('+ (Adição), - (Subtração), * (Mulitplicação), / (Divisão)')
print('** (Exponenciação)')
operacao = input('Digite a operacao da conta: ')

num2 = float(input('Digite outro número: '))

adicao = '+'
subtaracao = '-'
multiplicacao = '*'
divisao = '/'
expo = '**'

if operacao == adicao:
    print(num1 + num2)
elif operacao == subtaracao:
    print(num1 - num2)
elif operacao == multiplicacao:
    print(num1 * num2)
elif operacao == divisao:
    print(num1 / num2)
elif operacao == expo:
    print(num1 ** num2)

def verificaPositivo(valor):
    if (valor > 0):
        return 'P'
    else:
        return 'N'

numero = int(input('Informe um numero: '))
print (f'Resultado: {verificaPositivo(numero)}')

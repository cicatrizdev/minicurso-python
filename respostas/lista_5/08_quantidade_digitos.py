def quantidadeDigitos(digito):
    if (digito == 0):
        return 0
    return 1 + quantidadeDigitos(digito / 10)

# Fluxo Principal
digito = int(input('Informe um numero inteiro: '))
print (f'O numero {digito} possui {quantidadeDigitos(digito)}.')

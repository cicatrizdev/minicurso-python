import math

numInt1 = int(input('Informe um numero inteiro: '))
numInt2 = int(input('Informe outro numero inteiro: '))
numReal = float(input('Informe um numero real: '))

print (f'O dobro do primeiro vezes a metade do segundo é {(2 * numInt1) / (numInt2 / 2.0)}')
print (f'A soma do triplo do primeiro com o terceiro é {(3 * numInt1) + numReal}')
print (f'O terceiro elevado ao cubo é {math.pow(numReal, 3)}')

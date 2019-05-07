numero = int(raw_input('Informe o numero que voce quer ver a tabuada: '))

print (f'Tabuada do {numero}')
for i in range(1, 11):
    print (f'{numero}  X  {i}  =  {(numero * i)}')

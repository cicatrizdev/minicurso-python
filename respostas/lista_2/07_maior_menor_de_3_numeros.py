num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))
num3 = int(input('Informe mais um numero: '))

if (num1 == num2) and (num1 == num3):
    print ('Os numeros sao iguais')
else:
    if (num1 > num2) and (num1 > num3):
        print (f'O maior numero é: {num1}')
    elif (num2 > num3):
        print (f'O maior numero é: {num2}')
    else:
        print (f'O maior numero é: {num3}')

    if (num1 < num2) and (num1 < num3):
        print (f'O menor numero é: {num1}')
    elif (num2 < num3):
        print (f'O menor numero é: {num2}')
    else:
        print (f'O menor numero é: {num3}')

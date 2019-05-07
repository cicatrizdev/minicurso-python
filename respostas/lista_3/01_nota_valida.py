nota = -1
while (nota < 0) or (nota > 10):
    nota = int(input('Informe uma nota: '))
    if (nota < 0) or (nota > 10):
        print ('Nota Invalida')

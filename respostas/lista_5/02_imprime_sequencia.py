def imprime(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print j,
        print

numero = int(input('Informe um numero: '))
imprime(numero)

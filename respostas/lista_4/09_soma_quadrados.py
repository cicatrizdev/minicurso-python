a = []
for i in range(0, 10):
    a.append(int(input('Informe um numero: ')))

somaQuadrados = 0
for numero in a:
    somaQuadrados += (numero * numero)

print (f'A soma dos quadrados dos numeros lidos é: {somaQuadrados}')

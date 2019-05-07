numeros = []
for i in range(0, 4):
    numeros.append(int(input('Informe um numero inteiro: ')))

soma = 0
multiplicacao = 1
for i in numeros:
    soma += i
    multiplicacao *= i

print numeros
print (f'Soma dos numeros: {soma}')
print (f'Multiplicacao dos numeros: {multiplicacao}')

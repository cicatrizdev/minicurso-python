soma = 0
for i in range(0, 5):
    numero = int(raw_input('Informe um numero: '))
    soma += numero

print (f'A soma dos numeros digitados é: {soma}')
print (f'A media dos numeros digitados é: {(soma / 5.0)}')

inicial = int(input('Informe o valor inicial: '))
final = inicial
while (final <= inicial):
    final = int(input('Informe o valor final: '))
    if (final <= inicial):
        print ('O valor final deve ser maior que o valor final!')

soma = 0
for i in range(inicial, final + 1):
    soma += i
    print i

print (f'A soma dos numeros é: {soma}')

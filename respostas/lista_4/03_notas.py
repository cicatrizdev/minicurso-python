notas = []
for i in range(0, 4):
    notas.append(float(input('Informe uma nota: ')))

soma = 0.0
print '\nNotas Digitadas:'
for i in range(0, 4):
    print (f'Nota {i}: {notas[i].2f})
    soma += notas[i]

print (f'Media das notas: {(soma/4.0).2f}')

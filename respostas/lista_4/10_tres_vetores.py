vet1 = []
vet2 = []
vet3 = []

print ('Informe os valores do primeiro vetor')
for i in range(0, 10):
    vet1.append(int(input('Informe um numero: ')))

print ('Informe os valores do segundo vetor')
for i in range(0, 10):
    vet2.append(int(input('Informe um numero: ')))

for i in range(0, 10):
    vet3.append(vet1[i])
    vet3.append(vet2[i])

print vet3

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2.0

print (f'A media do aluno é: {media}')
if (media == 10):
    print ('Aprovado com Distincao')
elif (media >= 7):
    print ('Aprovado')
else:
    print ('Reprovado')

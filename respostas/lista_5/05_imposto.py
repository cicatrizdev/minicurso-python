def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto / 100.0)
    return custo

taxa = float(input('Informe o valor da taxa de imposto: '))
custo = float(input('Informe o custo do produto: '))

custo = somaImposto(taxa, custo)

print ('O preco com impostos é {custo})

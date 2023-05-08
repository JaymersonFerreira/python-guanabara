alturaParede = float(input('Altura da parede: '))
larguraParede = float(input('Largura da parede: '))
areaParede = alturaParede * larguraParede
boldeTinta = areaParede / 2
print('A área da parede é: {}, vai precisar de {} baldes de tinta para pintar a parede'.format(areaParede, boldeTinta))
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {:.3}x{:.3} e sua área é de {:.3}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
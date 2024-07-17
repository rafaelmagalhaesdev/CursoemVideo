medida = float(input('Uma distância em metros: '))
km = medida * 0.001
dec = medida * 0.1
dc = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de: {}m, equivale a {:.3f} km, {:.4f} Decametros, {:.1f} Centímetros e {:.3f} Milímetros'.format(medida, km, dec, dc, cm, mm))
medida = float(input('Qual o valor em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('O valor de {} m é o que vale: \n{} km \n{} hm \n{} dam \n{} dm \n{} cm \n{} mm '.format(medida, km, hm, dam, dm, cm, mm))
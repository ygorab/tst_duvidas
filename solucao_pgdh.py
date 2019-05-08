#coding: utf-8
import math

diametro = float(raw_input())
altura = float(raw_input())

raio = diametro / 2
area = (2 * math.pi * raio ** 2) + (2 * math.pi * raio * altura)

print 'Cálculo da Superfície de um Cilindro'
print '---'
print 'Medida do diâmetro? %.1f\nMedida da altura? %.1f\n---' % (diametro, altura)
print 'Área calculada: %.2f' % area




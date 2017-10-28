# -*- coding: utf-8 -*-
import os
import itertools

from time import time
from itertools import izip
from collections import OrderedDict

from funciones import initPass, generarF1, generarCandidato, genRules

#----------------------
#     VARIABLES
#----------------------
items_frecuentes = [] #Conjunto de todos los Fi
items_candidatos = [] #Conjunto de todos los Ci

indice = 1

#----------------------
#PARAMETROS DE ENTRADA.
#----------------------
soporte = 0.3
confianza = 0.8

start_time = time()

#----------------------
#  INICIO ALGORTIMO.
#----------------------
archivo = raw_input("Archivo: ")

file = open(archivo, 'r')

print('--------------------------')
print('Generando Candidato 1')
print('--------------------------')


C1, cant_transacciones = initPass(file)
items_candidatos.append(C1) #Cargo a C1 en items_candidatos

print('--------------------------')
print('Generando Items frecuentes 1')
print('--------------------------')
F1 = generarF1(soporte, cant_transacciones, C1)

items_frecuentes.append(F1) #Cargo en items_frecuentes a F1

#archivo = raw_input("Archivo: ")
file = open(archivo, 'r')					

f_i  = F1
while (f_i):

	print('\n\n\n\--------------------------')
	print('Generando Candidato ' + str(indice + 1))	
	print('--------------------------')
	candidato_i = generarCandidato(items_frecuentes[indice - 1])
	
	file = open(archivo, 'r')	
	for t in file:
		transaccion = t
		transaccion = transaccion.split()
		for c in candidato_i[:]:
			candidatos = c[0]
			candidatos = candidatos.split()
			if set(candidatos).issubset(transaccion):
				c[1] = c[1] + 1
	
	items_candidatos.append(candidato_i)
	
	f_i = list()
	f_aux= list()
	print('--------------------------')
	print('Generando Items frecuentes ' + str(indice + 1))	
	print('--------------------------')
	for c in candidato_i[:]:
		if float(c[1])/float(cant_transacciones) >= soporte:
			f_i = list()
			f_i.append(c[0])
			f_i.append(c[1])
			f_aux.append(f_i)
			
	#items_frecuentes.append(f_i)
	items_frecuentes.append(f_aux)
	indice = indice + 1


genRules(items_frecuentes, confianza)

elapsed_time = time() - start_time
print("Tiempo transcurrido: %.2f seg." % elapsed_time)
print("Tiempo transcurrido: %.2f min." % (elapsed_time/60))

#print('Cantidad de Transaciones: ', cant_transacciones)
#print('Cantidad de Productos: ', len(C1))



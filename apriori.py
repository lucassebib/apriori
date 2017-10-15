# -*- coding: utf-8 -*-
import os
import itertools

from time import time
from itertools import izip
from collections import OrderedDict

from funciones import initPass, generarF1, generarCandidato

#Variables
items_frecuentes = [] #Conjunto de todos los Fi

#----------------------
#Parametros de Entrada.
#----------------------
soporte = 0.3
confianza = 0.8

start_time = time()


archivo = raw_input("Archivo: ")
file = open(archivo, 'r')

C1, cant_transacciones = initPass(file)
F1 = generarF1(soporte, cant_transacciones, C1)
items_frecuentes.append(F1) #Cargo en items_frecuentes a F1
					
indice = 1

#while (len(items_frecuentes[indice - 1])):
	
candidato_i = generarCandidato(items_frecuentes[indice - 1])

elapsed_time = time() - start_time

#print(candidato_i)

#a = [('cerveza', 4), ('jamon', 5), ('pan', 3), ('queso', 4)]
#print(a.__class__)
#print(F1)
#print(F1.__class__)
	#indice=+ 1

print("Tiempo transcurrido: %.2f seg." % elapsed_time)
print("Tiempo transcurrido: %.2f min." % (elapsed_time/60))

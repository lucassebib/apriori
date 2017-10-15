# -*- coding: utf-8 -*-
import os
import itertools


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

archivo = raw_input("Archivo: ")
file = open(archivo, 'r')

C1, cant_transacciones = initPass(file)
F1 = generarF1(soporte, cant_transacciones, C1)
print(F1)
items_frecuentes.append(F1) #Cargo en items_frecuentes a F1
					
indice = 1

#while (len(items_frecuentes[indice - 1])):
	
candidato_i = generarCandidato(items_frecuentes[indice - 1], indice + 1)
print(candidato_i)
	#indice=+ 1


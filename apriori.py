# -*- coding: utf-8 -*-
#import time
#from datetime import datetime
import operator
from itertools import izip
from collections import OrderedDict

#Variables
c1 = {}
transacciones = 0

#----------------------
#Parametros de Entrada.
#----------------------
soporte = 0.3
confianza = 0.8

archivo = raw_input("Archivo: ")
file = open(archivo, 'r')

#----------------------
# PASO 1:
# LEE EL ARCHIVO Y GENERA DOS LISTAS: 
# UNO C1 con Todos los productos distintos y 
# otra lista soportes con el valor de soporte de cada elemento de C1
#----------------------
for linea in file:
	transacciones+= 1
	linea = linea.split()
	for li in linea:
		if not li in c1:
			c1.update({li:1})
		else:
			c1[li] = c1[li] + 1 

#----------------------
#PASO 3: Ordeno lexicograficamente
#Genero una tupla de dos elementos donde el primero tiene el producto y el segundo el soporte
#----------------------
dicc = sorted(c1.items(), key=operator.itemgetter(0))

#----------------------
#PASO 3: Elimino los elementos de ambas listas que no superan soporte y confianza
#----------------------







# -*- coding: utf-8 -*-
import os
import itertools

from time import time
from itertools import izip
from collections import OrderedDict

from funciones import initPass, generarF1, generarCandidato, genRules, obtener_cantReglas

cant_transacciones = 0
cant_productos = 0

def EjecutarCorrida (archivo, suport, conf):
	#----------------------
	#     VARIABLES
	#----------------------
	items_frecuentes = [] #Conjunto de todos los Fi
	items_candidatos = [] #Conjunto de todos los Ci
	soporte = float(suport/100)
	confianza= float(conf/100)

	indice = 1
	#TOTAL_LINEAS = sum(1 for line in open(file))
	#----------------------
	#  INICIO ALGORTIMO.
	#----------------------
	#archivo = raw_input("Archivo: ")

	file = open(archivo, 'r')

	print('--------------------------------')
	print('PASO 1: Lectura de Archivo OK')
	global cant_transacciones
	C1, cant_transacciones = initPass(file)
	items_candidatos.append(C1) #Cargo a C1 en items_candidatos
	global cant_productos
	cant_productos = len(C1)

	print('--------------------------------')
	print('PASO 2: INITPASS')
	print(str(cant_transacciones))

	F1 = generarF1(soporte, cant_transacciones, C1)
	print(F1)
	items_frecuentes.append(F1) #Cargo en items_frecuentes a F1


	file = open(archivo, 'r')					

	f_i  = F1
	while (f_i):
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

		for c in candidato_i[:]:
			if float(c[1])/float(cant_transacciones) >= soporte:
				f_i = list()
				f_i.append(c[0])
				f_i.append(c[1])
				f_aux.append(f_i)
				
		#items_frecuentes.append(f_i)
		items_frecuentes.append(f_aux)
		print(f_aux)
		print('--------------------------')
		print('GENERANDO F' + str(indice) )
		indice = indice + 1


	print('--------------------------')
	print('GENERANDO REGLAS' )	
	genRules(items_frecuentes, confianza)

	file.close()
def obtenerDatos():
	global cant_transacciones
	global cant_productos
	cant_relgas = obtener_cantReglas()
	return cant_transacciones, cant_productos, cant_relgas




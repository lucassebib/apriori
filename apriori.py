# -*- coding: utf-8 -*-

archivo = raw_input("Archivo: ")
transacciones = []
id_transaccion = 0
file = open(archivo, 'r')
for linea in file:
	linea = linea.split()
	id_transaccion+= 1
	for l in linea:
		transacciones.append(id_transaccion)
		transacciones.append(l)
print(transacciones)







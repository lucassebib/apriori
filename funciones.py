import operator
import math
import itertools

def initPass(archivo_transacciones):
	#---------------------------------------------------------------------------
	# PASO 1:
	# LEE EL ARCHIVO Y GENERA UN DICCIONARIO candidatos_ini DONDE: 
	# La clave son Todos los productos distintos y 
	# el valor es el soportes (X.count()) de cada elemento de candidatos_ini
	#---------------------------------------------------------------------------
	candidatos_ini = {}
	cant_transacciones = 0

	for linea in archivo_transacciones:
		cant_transacciones+= 1
		linea = linea.split()
		for li in linea:
			if not li in candidatos_ini:  #La primera vez que selecciono el producto
				candidatos_ini.update({li:1}) #Cargo un diccionario con el producto y el soporte inicializado en 1 EJ: {'papa': 1}
			else: #Ya estaba en lista por lo que solo tengo que incrementar el soporte
				candidatos_ini[li] = candidatos_ini[li] + 1 

	#---------------------------------------------------------------------------
	#PASO 2: Ordeno lexicograficamente obteniendo c1
	#Genero una lista (C1) de dos elementos cada uno, donde el primero tiene el producto y el segundo el soporte
	#---------------------------------------------------------------------------
	C1 = sorted(candidatos_ini.items(), key=operator.itemgetter(0))

	return C1, cant_transacciones

def generarF1(soporte, cant_transacciones, C1):
	#----------------------
	#PASO 3: Elimino los elementos de ambas listas que no superan soporte y confianza
	#En este paso obtendria F1
	#----------------------
	F1 = C1
	min_soporte = int(math.ceil(cant_transacciones*soporte)) #Si hay decimales rendondeo siempre hacia arriba
	for product in F1[:]:
		#Si no cumple con el minimo de Soporte lo elimino de la lista
		if product[1] < min_soporte:
			F1.remove(product)

	return F1

def obtener_primeros_elementos(lista):
	return lista.insert(0, '*****').remove(lista[len(lista-1)])

def generarCandidato(item_frecuente, indice):
	for item in item_frecuente:
		item_frecuentes_siguientes = item_frecuente
		item_frecuentes_siguientes.append(item)
		for item_sig in item_frecuentes_siguientes:
			primeros_elementos_item = obtener_primeros_elementos(item)
			primeros_elementos_item_sig = obtener_primeros_elementos(item)
			print(primeros_elementos_item)
			#ultimo_elemento_item
			#ultimo_elemento_item_sig 
		#print(item)
	return indice

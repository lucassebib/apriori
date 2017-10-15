import operator
import math
import itertools

from subfunciones import obtener_primeros_elementos, obtener_ultimo_elemento, comprar_listas

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
	#Retorna: Lista
	#Ejemplo: ['cerveza', 'jamon', 'pan', 'queso']
	#----------------------
	F1 = []
	min_soporte = int(math.ceil(cant_transacciones*soporte)) #Si hay decimales rendondeo siempre hacia arriba
	for product in C1[:]:
		#Si no cumple con el minimo de Soporte lo elimino de la lista
		if not product[1] < min_soporte:
			F1.append(product[0])	
	return F1

def generarCandidato(item_frecuente):
	#---------------------------------------------------------------------------
	#PASO 4: Genera Candidato i
	# Cada posicion reprensenta una tupla de dos elementos:
	# El primer elemento de la tupla es un string con los productos
	# El segudo es un entero con la cantidad de coincidencias en las transacciones
	#RETORNA: Lista
	#[('cerveza jamon pan', 0), ('cerveza jamon queso', 0), ('cerveza pan queso', 0), ('jamon pan queso', 0)]
	#---------------------------------------------------------------------------
	
	#item_frecuente = ['beef cheese', 'beef chicken', 'chicken clothes', 'chicken milk', 'clothes milk']
	#item_frecuente = ['cerveza jamon', 'cerveza pan', 'cerveza queso', 'jamon pan', 'jamon queso', 'pan queso']
	itemset = list(item_frecuente)
	
	c = list()
	linea_siguiente = item_frecuente
	
	for item in item_frecuente[:]:
		linea_siguiente.remove(item)
		for item_sig in linea_siguiente[:]:
			primeros_elementos_item = obtener_primeros_elementos(item)
			primeros_elementos_item_sig = obtener_primeros_elementos(item_sig)
			
			ultimo_elemento_item = obtener_ultimo_elemento(item)
			ultimo_elemento_item_sig = obtener_ultimo_elemento(item_sig)

			if (comprar_listas(primeros_elementos_item, primeros_elementos_item_sig)) and not(ultimo_elemento_item==ultimo_elemento_item_sig):
				t = tuple()
				t = (item + ' ' + ultimo_elemento_item_sig, 0)				
				c.append(t)

	for li in c[:]: #li tendra un string con todos los productos. Ej: 'cerveza jamon pan'
		linea = li[0].split() #Retorna una lista donde cada elemento sera un string con los valores de li. Ej: ['cerveza', 'jamon', 'pan']
		
		for indice in range(0,len(linea)): #Armo las distintas combinacion de elementos y los guardo en cadena. Ej: 'cerveza jamon' 'cerveza pan' 'jamon pan'
			cadena = str()							   # Para armar las combinaciones solamente basta eliminar la diagonal principal
			for i, x in enumerate(linea):              # *cerveza* jamon pan
				if not i == indice:					   # cerveza *jamon* pan
					cadena = cadena + ' '+ str(x)      # cerveza jamon *pan*
			cadena = cadena.strip()
			
			if not cadena in itemset:
				c.remove(li)
	
	return c

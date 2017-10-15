def obtener_primeros_elementos(lista):
	#---------------------------------------------------------------------------
	#Funcion: devuleve los primeros elementos de la lista que se recibe como parametro
	#		  previamente inserta en la primera posicion un elemento distintivo que representara al vacio		  
	#         eliminando el ultimo elemento
	#RETORNA: Lista
	#EJEMPLO: ['*****', 'pan']
	#---------------------------------------------------------------------------
	salida = lista.split()
	salida.pop(len(salida)-1)
	salida.insert(0, '*****')
	return salida

def obtener_ultimo_elemento(lista):
	#---------------------------------------------------------------------------
	#Funcion: devuleve la ultima posicion de la lista pasada como parametro
	#RETORNA: String
	#---------------------------------------------------------------------------
	salida = lista.split()
	return salida[len(salida)-1]

def comprar_listas(lista_a, lista_b):
	#---------------------------------------------------------------------------
	#Funcion: Compara dos listas, si son iguales retorna True, sino False
	#RETORNA: Booleano
	#---------------------------------------------------------------------------
	for i in range(0,len(lista_a)):
		if(lista_a[i] != lista_b[i]):
			return False
	return True
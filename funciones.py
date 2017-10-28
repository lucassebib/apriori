import os
import sys
import operator
import math
import itertools
import time

from subfunciones import obtener_primeros_elementos, obtener_ultimo_elemento, comparar_listas



archivo_salida = open('reglas/reglas'+ str(time.strftime("%H%M%S")) + '.dat', 'w')

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
	#Ejemplo: [['cerveza', 3], ['jamon', 2], ['pan', 5], ['queso', 6]]
	#----------------------
	F1 = []
	min_soporte = int(math.ceil(cant_transacciones*soporte)) #Si hay decimales rendondeo siempre hacia arriba
	for product in C1[:]:
		#Si no cumple con el minimo de Soporte lo elimino de la lista
		if not product[1] < min_soporte:
			f_aux= list()
			f_aux.append(product[0])
			f_aux.append(product[1])
			F1.append(f_aux)	
	return F1





	#return sorted(F1.items(), key=operator.itemgetter(0)) #devuelve [('cerveza', 4), ('jamon', 5), ('pan', 3), ('queso', 4)]

def generarCandidato(item_frecuente):
	#---------------------------------------------------------------------------
	#PASO 4: Genera Candidato i
	# Cada posicion reprensenta una lista de dos elementos:
	# El primer elemento de la lista es un string con los productos
	# El segudo es un entero con la cantidad de coincidencias en las transacciones
	#RETORNA: Lista
	#[['cerveza jamon pan', 0], ['cerveza jamon queso', 0], ['cerveza pan queso', 0], ['jamon pan queso', 0]]
	#---------------------------------------------------------------------------
	
	#item_frecuente = ['beef cheese', 'beef chicken', 'chicken clothes', 'chicken milk', 'clothes milk']
	#item_frecuente = ['cerveza jamon', 'cerveza pan', 'cerveza queso', 'jamon pan', 'jamon queso', 'pan queso']

	#itemset = list(item_frecuente)
	itemset= list()
	for item in item_frecuente:
		itemset.append(item[0])

	c = list()
	linea_siguiente = list(item_frecuente)
	
	for item in item_frecuente[:]:
		linea_siguiente.remove(item)
		for item_sig in linea_siguiente[:]:
			primeros_elementos_item = obtener_primeros_elementos(item[0])
			primeros_elementos_item_sig = obtener_primeros_elementos(item_sig[0])
			
			ultimo_elemento_item = obtener_ultimo_elemento(item[0])
			ultimo_elemento_item_sig = obtener_ultimo_elemento(item_sig[0])

			if (comparar_listas(primeros_elementos_item, primeros_elementos_item_sig)) and not(ultimo_elemento_item==ultimo_elemento_item_sig):
				l = list()
				l.append(item[0] + ' ' + ultimo_elemento_item_sig)
				l.append(0)				
				c.append(l)

	for li in c[:]: #li tendra un string con todos los productos. Ej: 'cerveza jamon pan'
		linea = li[0].split() #Retorna una lista donde cada elemento sera un string con los valores de li. Ej: ['cerveza', 'jamon', 'pan']
		
		for indice in range(0,len(linea)): #Armo las distintas combinacion de elementos y los guardo en cadena. Ej: 'cerveza jamon' 'cerveza pan' 'jamon pan'
			cadena = str()							   # Para armar las combinaciones solamente basta eliminar la diagonal principal
			for i, x in enumerate(linea):              # ***cerveza***     jamon            pan         ---> jamon pan
				if not i == indice:					   #    cerveza        ***jamon***      pan         ---> cerveza pan
					cadena = cadena + ' '+ str(x)      #    cerveza           jamon       ***pan***     ---> cerveza jamon
			cadena = cadena.strip()
			
			li_bk = li 
			if not cadena in itemset: 
				try:
					c.remove(li_bk)
				except Exception as e:
					pass
				
	return c

def genRules(frecuentes, minConfianza): 
	#---------------------------------------------------------------------------
	# 
	# 
	# 
	#
	#
	#---------------------------------------------------------------------------
	
	

	for idx, F_i in enumerate(frecuentes[1:]): #frecuentes[1:] indica que arranca desde la posicion 1 de F (tener en cuenta que los indeces arrancan 0)	
		for li in F_i: #li tendra un string con todos los productos. Ej: ['cerveza jamon', 4] de F_i
			H1= list()
			linea = li[0].split() #Retorna una lista donde cada elemento sera un string con los valores de li. Ej: ['cerveza', 'jamon']
			soporteRegla= li[1]
			soporteAntecedente= 0 #Inicializo la variable 
			for indice in range(0,len(linea)):                 #Armo las distintas combinacion de elementos para obtener el antecedente y consecuente
				antecedente = str()							   # En este caso el consecuente seria el elemento de la diagonal principal
				consecuente= str()
				for i, x in enumerate(linea):              		  # ***cerveza***     jamon          pan         \\  jamon pan --> cerveza
					if not i == indice:					  	      #    cerveza     ***jamon***       pan         \\  cerveza pan --> jamon
						antecedente = antecedente + ' '+ str(x)   #    cerveza        jamon       ***pan***      \\ cerveza jamon ---> pan
					else:
						consecuente= str(x)
				antecedente = antecedente.strip()
				consecuente = consecuente.strip()
				
				for item in frecuentes[idx]:    #Recorro el F_i para encontrar el antecedente y encontrar su soporte
					if item[0] == antecedente:
						soporteAntecedente= item[1]

				conf= float(soporteRegla)/float(soporteAntecedente)
				
				if conf >= minConfianza:
					archivo_salida.write(antecedente + ' ---> ' + consecuente + os.linesep)
					h_aux= list()
					h_aux.append(consecuente)
					h_aux.append(0)
					H1.append(h_aux) #Guarda todos los consecuentes que tiene un elemento
			

			apGenRules(li, H1, frecuentes, minConfianza)



def apGenRules(fk, Hm, F, minConfianza): #fk tiene la forma ['cerveza jamon pan', 2]....Hm tiene la forma [['cerveza', 0], ['jamon', 0], ['pan', 0]]
	k= len(fk[0].split()) #obtiene el valor de k calculando la longitud que tiene el primer elemento del itemset fk

	if len(Hm)>0:
		m= len(Hm[0][0].split()) # obtiene el valor de m calculando la longitud que tiene el primer elemento de Hm. Hm tiene 

	if (len(Hm) != 0) and (k > m+1):
		Hm_mas_1= generarCandidato(Hm) #Hm_mas_1 tiene [['cerveza jamon', 0], ['cerveza pan', 0], ['jamon pan', 0]]
		for hm_mas_1 in Hm_mas_1: #hm_mas_1 tien la forma ['cerveza jamon', 0]
			list_fk = fk[0].split() #Se tiene ['cerveza', 'jamon', 'pan']
			list_hm_mas_1= hm_mas_1[0].split() #Se tiene ['cerveza', 'jamon']
			antecedente=list()
			for elem in list_fk:
				if elem not in list_hm_mas_1:
					antecedente.append(elem)
			consecuente= hm_mas_1[0]
			soporteConsecuente=0

			for item in F[len(antecedente)-1]: #Recorremos el F anterior para buscar el soporte del antecedente
		
				el1=item[0].split()
				el2= antecedente
				if el1==el2:
					soporteConsecuente=item[1]
			conf= float(fk[1])/float(soporteConsecuente)
			if conf> minConfianza:
				archivo_salida.write(str(antecedente).replace('[','').replace(']','').replace('\'','') +"-->"+ str(consecuente) + os.linesep)
			else:
				Hm_mas_1.remove(hm_mas_1)
		apGenRules(fk, Hm_mas_1, F, minConfianza)
	
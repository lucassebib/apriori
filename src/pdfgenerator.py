# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import os
import time

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

#from UiMenuPrincipal import cant_reglas, cant_transacc
from apriori import obtenerDatos

RUTA_BASE = os.path.dirname(os.path.dirname(__file__))
RUTA_REGLAS = os.path.join(RUTA_BASE, 'reglas')

nombre_pdf = 'informeAppRules.pdf'


def generarPDF():
	archivo_reglas = open(RUTA_REGLAS + '/reglas' + '.dat', 'r')

	
	fecha = time.strftime("%d/%m/%y")
	hora = time.strftime("%H:%M:%S")

	pdf = canvas.Canvas(nombre_pdf, pagesize=letter)
	pdf.setLineWidth(.3)
	pdf.setFont('Helvetica', 12)
	 
	pdf.drawString(30,750,'appRules©2017')
	pdf.drawString(30,735,'INFORME DE REGLAS')
	pdf.drawString(500,750,hora + ' ' + fecha)
	#pdf.line(480,747,580,747)
	
	pdf.drawCentredString (30,710,'REGLAS SIN RESTRICCIONES')
	pos = 700

	for linea in archivo_reglas:
		l = linea[:len(linea) - 1]
		pdf.drawString(100, pos , l) 
		pos = pos -40


	pdf.save()

	#os.system(nombre_pdf)
	os.popen(nombre_pdf)


def generaratePDF():
	fecha = time.strftime("%d/%m/%y")
	hora = time.strftime("%H:%M:%S")

	archivo_reglas = open(RUTA_REGLAS + '/reglas' + '.dat', 'r')
	doc = SimpleDocTemplate(nombre_pdf, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
	doc.pagesize = landscape(A4)
	elements = []

	data = list()
	fila = list()
	fila.append('Regla')
	fila.append('Soporte')
	fila.append('Confianza')
	data.append(fila)

	for linea in archivo_reglas:
		l = linea.split()
		soporte = l[len(l) - 4]
		confianza = l[len(l) - 3]

		item = str()
		for k, j in enumerate(l):
			if k < len(l) - 4:
				item = item + " " + j
			else: 
				break;
		
		l = item.split('--->')
		print(l)
		fila = list()
		fila.append(str(l[0]) + " ---> " + str(l[1]))
		fila.append(str(float(soporte)))
		fila.append(str((float(confianza)))) 
		data.append(fila)
	
	archivo_reglas.close()
	#TODO: Get this line right instead of just copying it from the docs
	style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
	                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
	                       ('VALIGN',(0,0),(0,-1),'TOP'),
	                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
	                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
	                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
	                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
	                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
	                       ])
	 
	#Configure style and word wrap
	s = getSampleStyleSheet()
	s = s["BodyText"]
	s.wordWrap = 'CJK'
	data2 = [[Paragraph(cell, s) for cell in row] for row in data]
	t=Table(data2)
	t.setStyle(style)
	 
	#Send the data and build the file
	styleFechaHora = ParagraphStyle(name='Normal',fontSize=10,alignment=TA_RIGHT,spaceAfter=10)
	styleTitulo = ParagraphStyle(name='Normal',fontSize=18,alignment=TA_CENTER,spaceAfter=10)
	styleCantReglasItemTrans = ParagraphStyle(name='Underline',fontSize=14,alignment=TA_LEFT,spaceAfter=5)

	cant_transacciones, cant_items, cant_reglas = obtenerDatos()
	elements.append(Paragraph(fecha +" "+hora , style = styleFechaHora))
	elements.append(Paragraph("<u>Informe de reglas de asociacion</u>", style = styleTitulo))
	elements.append(Paragraph("Total de items: "+str(cant_items), style = styleCantReglasItemTrans))
	elements.append(Paragraph("Total de transacciones: "+str(cant_transacciones), style = styleCantReglasItemTrans))
	elements.append(Paragraph("Reglas generadas: "+str(cant_reglas), style = styleCantReglasItemTrans))
	elements.append(Paragraph("", style = styleCantReglasItemTrans))
	elements.append(t)
	doc.build(elements)
	
	os.popen(nombre_pdf)



 

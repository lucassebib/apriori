# -*- coding: utf-8 -*-

import os
import time

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

RUTA_BASE = os.path.dirname(os.path.dirname(__file__))
RUTA_REGLAS = os.path.join(RUTA_BASE, 'reglas')

nombre_pdf = 'informeAppRules.pdf'
archivo_reglas = open('reglas' + '.dat', 'r')

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

#!/usr/local/bin/python
 
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
 
doc = SimpleDocTemplate(nombre_pdf, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
doc.pagesize = landscape(A4)
elements = []

data = list()
fila = list()
fila.append('Regla')
fila.append('Soporte')
fila.append('Confianza')

for linea in archivo_reglas:
	l = linea.split()
	fila = list()
	fila.append(l[0])
	fila.append(l[1])
	fila.append(l[2])
	data.append(fila)
 
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
elements.append(t)
doc.build(elements)


 

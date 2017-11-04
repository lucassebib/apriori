# -*- coding: utf-8 -*-

import os
import time

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

RUTA_BASE = os.path.dirname(os.path.dirname(__file__))
RUTA_REGLAS = os.path.join(RUTA_BASE, 'reglas')


def generarPDF():
	archivo_reglas = open(RUTA_REGLAS + '/reglas' + '.dat', 'r')

	nombre_pdf = 'informeAppRules.pdf'
	fecha = time.strftime("%d/%m/%y")
	hora = time.strftime("%H:%M:%S")

	pdf = canvas.Canvas(nombre_pdf, pagesize=letter)
	pdf.setLineWidth(.3)
	pdf.setFont('Helvetica', 12)
	 
	pdf.drawString(30,750,'appRules©2008')
	pdf.drawString(30,735,'INFORME DE REGLAS')
	pdf.drawString(500,750,hora + ' ' + fecha)
	pdf.line(480,747,580,747)
	
	pdf.drawString(30,710,'REGLAS SIN RESTRICCIONES')
	pos = 600
	for linea in archivo_reglas:
		pdf.drawString(100, pos , linea) 
		pos = pos -40


	pdf.save()

	os.system(nombre_pdf)


 

#Assignment 9

#PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
#	- Search for available PDF library that you can use
#	- Search how data is structured using JSON format
#	- Search how to read JSON file
#	- You will create the JSON file manually
#	- Your code should be in github before Feb12

import json
from fpdf import FPDF

pdf= FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.image('bg.png',x = -0.5, y= -0.5, w = pdf.w + 1)

jsonPDF = open('personaldeets.json', 'r')
read = jsonPDF.read()
infos = json.loads(read)

pdf.output('VELASQUEZ_DANIELLAFRANCINE.pdf')

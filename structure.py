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
from turtle import width
from fpdf import FPDF

with open('personaldeets.json') as jsonFILE:
    resumedata= json.load(jsonFILE)

name= resumedata["complete_name"]
gender= resumedata["gender_sex"]
age= resumedata["age"]
address= resumedata["home_address"]
primaryeducation= resumedata["primaryeducation_basic"]
secondaryeducation= resumedata["secondaryeducation_middle"]
tertiaryeducation= resumedata["tertiaryeducation_high school"]
college= resumedata["college"]
masteraldegree= resumedata["masteral_degree"]
achievement1= resumedata["achievement1"]
achievement2= resumedata["achievement2"]
achievement3= resumedata["achievement3"]
achievement4= resumedata["achievement4"]
achievement5= resumedata["achievement5"]
achievement6= resumedata["achievement6"]
skills1= resumedata["skills1"]
skills2= resumedata["skills2"]
skills3= resumedata["skills3"]
skills4= resumedata["skills4"]
skills5= resumedata["skills5"]
skills6= resumedata["skills6"]
mobnumber= resumedata["mobile_number"]
emailaddress= resumedata["email_address"]
telnumber= resumedata["telephone_number"]
title=resumedata['title']

resume= FPDF('P', 'mm', 'Letter')
resume.add_page() # dds a page within the PDF file
resume.image('bg.png', x = -0.5, y= -0.5, w = resume.w + 1) # i added a background image for design (most resume examples have their own bg design)

resume.set_font('Helvetica', 'B', 30)
resume.image('2x2.png', 10, 13, 40, 0) # my picture, located at the top right corner of the file
resume.set_text_color(255,255,255) # white font color in contrast with the partial color of the background
resume.set_margins(top=20, left=20, right=20)
resume.cell(220, 15, title,  align='C', ln=True)
resume.image('line.png', x = 41, y= 0, w = resume.w -10) # line for design

resume.set_font('helvetica', 'B', 18)
resume.set_text_color(0,0,0) # set font color to black once again to contrast light colors of the background
resume.cell(0, 20, "", align='L', ln=True) # cell division to manage the space
resume.cell(0, 15, "Primary Information", align='L', ln=True) #title
resume.set_font('courier', '', 13)
resume.cell(0, 2,"Complete Name     : " + str(resumedata["complete_name"]), align='L', ln=True)
resume.cell(0, 7,"Gender / Sex      : " + str(resumedata["gender_sex"]), align='L', ln=True)
resume.cell(0, 3,"Age               : " + str(resumedata["age"]), align='L', ln=True)
resume.cell(0, 6,"Home Address      : " + str(resumedata["home_address"]), align='L', ln=True)

resume.set_font('helvetica', 'B', 18) # helvetica font, set to bold, 18 fsize
resume.cell(0,15, "Academic Background", align='L', ln=True) # title
resume.set_font('courier','', 13) # courier font, no emphasis, 13 fsize
resume.cell(0, 2,"Primary Education    : " + str(resumedata["primaryeducation_basic"]), align='L', ln=True)
resume.cell(0, 8,"Secondary Education  : " + str(resumedata["secondaryeducation_middle"]), align='L', ln=True)
resume.cell(0, 4,"Tertiary Education   : " + str(resumedata["tertiaryeducation_high school"]), align='L', ln=True)
resume.cell(0, 7,"College              : " + str(resumedata["college"]), align='L', ln=True)
resume.cell(0, 6,"Masteral Degree      : " + str(resumedata["masteral_degree"]), align='L', ln=True)
resume.line(20, 90, 160, 90) # line for pdf after each cell

resume.set_font('helvetica', 'B', 18) # for the title, helvetica, set to bold, 18 fsize
resume.cell(0,15, "Achievements", align='L', ln=True) # title
resume.set_font('courier','', 13) # courier font, no emphasis, 13 fsize
resume.cell(0, 2,"a.  " + str(resumedata["achievement1"]), align='L', ln=True)
resume.cell(0, 8,"b.  " + str(resumedata["achievement2"]), align='L', ln=True)
resume.cell(0, 4,"c.  " + str(resumedata["achievement3"]), align='L', ln=True)
resume.cell(0, 7,"d.  " + str(resumedata["achievement4"]), align='L', ln=True)
resume.cell(0, 6,"e.  " + str(resumedata["achievement5"]), align='L', ln=True)
resume.cell(0, 6,"f.  " + str(resumedata["achievement6"]), align='L', ln=True)
resume.line(20, 132, 160, 132) # line for pdf after each cell

resume.set_font('helvetica', 'B', 18) # for the title, helvetica, set to bold, 18 fsize
resume.cell(0,15, "Skills", align='L', ln=True) # title
resume.set_font('courier','', 13) # courier font, no emphasis, 13 fsize
resume.cell(0, 2,"a.  " + str(resumedata["skills1"]), align='L', ln=True)
resume.cell(0, 8,"b.  " + str(resumedata["skills2"]), align='L', ln=True)
resume.cell(0, 4,"c.  " + str(resumedata["skills3"]), align='L', ln=True)
resume.cell(0, 7,"d.  " + str(resumedata["skills4"]), align='L', ln=True)
resume.cell(0, 6,"e.  " + str(resumedata["skills5"]), align='L', ln=True)
resume.cell(0, 6,"f.  " + str(resumedata["skills6"]), align='L', ln=True)
resume.line(20, 180, 160, 180) # line for pdf after each cell

resume.set_font('helvetica', 'B', 18) # for the title, helvetica, set to bold, 18 fsize
resume.cell(0,15, "Contact Information", align='L', ln=True) # title
resume.set_font('courier','', 13) # courier font, no emphasis, 13 fsize
resume.cell(0, 2,"Email Address     :  " + str(resumedata["email_address"]), align='L', ln=True)
resume.cell(0, 8,"Mobile Number     :  " + str(resumedata["mobile_number"]), align='L', ln=True)
resume.cell(0, 4,"Telephone Number  :  " + str(resumedata["telephone_number"]), align='L', ln=True)
resume.line(20, 227, 160, 227) # line for pdf after each cell

# saves the pdf with the program code along with its stated filename
resume.output('VELASQUEZ_DANIELLAFRANCINE.pdf') 

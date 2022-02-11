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
resume.add_page()
resume.image('bg.png', x = -0.5, y= -0.5, w = resume.w + 1)

resume.output('VELASQUEZ_DANIELLAFRANCINE.pdf')

import csv
import pdfplumber
import os

file = 'C:\\Users\\rajes\\Desktop\\upwork1test'

for filename in os.listdir(file):
    if filename.endswith(".pdf"):
         final = []
         with pdfplumber.open(file + '\\' + filename) as pdf:
             pages = pdf.pages
             for page in pdf.pages:
                 text = page.extract_text()
                 for line in text.split('\n'):
                     final.append(line.split(' '))
         with open(file + f"\\{filename.split('.')[0]}.csv", "w") as fp:
             wr = csv.writer(fp, lineterminator='\n')
             wr.writerows(final)


# #pip install pyttsx3
# # pip install PyPDF2

# # importing all the required modules

import pyttsx3
import PyPDF2

# # creating an object 
# file = open('example.pdf', 'rb')

# # creating a pdf reader object
# fileReader = PyPDF2.PdfFileReader(file)

# # print the number of pages in pdf file
# print(fileReader.numPages)

book = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()













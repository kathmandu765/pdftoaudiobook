import pyttsx3
import PyPDF2
book = open('html.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()



# #install pyDF2
# # pip install PyPDF2

# # importing all the required modules
# import PyPDF2

# # creating an object 
# file = open('html.pdf', 'rb')

# # creating a pdf reader object
# fileReader = PyPDF2.PdfFileReader(file)

# # print the number of pages in pdf file
# print(fileReader.numPages)

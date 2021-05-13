# type 'pip insall PyPDF2' and 'pip install pyttsx3' in cmd to install given modules
import PyPDF2
import pyttsx3
import os

os.system('cls')

# function to read loud the pdf
def readPDF():
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)     
    engine.setProperty('rate',175)
    engine.say(page_content)
    engine.runAndWait()

#set your document or pdf path here-
try:
    doc_path=input('Enter the path of pdf:')
    doc=open(doc_path,'rb')

    pdf=PyPDF2.PdfFileReader(doc,strict=False)

    # getting number of pages in a pdf
    number_of_pages=pdf.getNumPages()
    
    # printing number of pages in a pdf
    print(f'\nNumber of pages:{number_of_pages}\n\n')

    for page in range(0,number_of_pages):
        current_page= pdf.getPage(page)
        # extracting text from page
        page_content = current_page.extractText()
        # printing the page content
        print(f'Page Content:\n\n{page_content}')
        readPDF()
except:
    print('Operation Failed...!')

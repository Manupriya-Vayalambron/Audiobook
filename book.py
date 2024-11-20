import pyttsx3
import PyPDF2

file=open("story.pdf","rb")
pdf_reader=PyPDF2.PdfReader(file)
total=len(pdf_reader.pages)
print(total)
melo=pyttsx3.init()
for i in range(14,total):
    page=pdf_reader.pages[i]
    text=page.extract_text()
    sentences = text.split('.')
    for sentence in sentences:
        if sentence:
            melo.say(sentence)
            print(sentence)
            melo.runAndWait()

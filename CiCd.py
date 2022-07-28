from docx2pdf import convert
import os
DocPath = r"C:\Users\benba\Ben Bar\CV - Ben Bar.docx"
PdfPath = r"C:\Users\benba\Ben Bar\CV - Ben Bar.pdf"
print("Converting the word file to pdf..")
convert(DocPath)
print("pushing both docs to the repo..")
commit = input("Please type the commit: ")
os.system("powershell git add .")
os.system("powershell git commit -m " + commit)
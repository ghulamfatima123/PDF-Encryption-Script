from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwritter = PdfWriter()
pdf = PdfReader("ghulam_fatima_resume.pdf")

for page_num in range(pdf.numPages):
    pdfwritter.addPage(pdf.getPage(page_num))

passw = getpass.getpass(prompt="Enter Password : ")
pdfwritter.encrypt(passw)

with open("MyResumeProtected.pdf", "wb") as f:
    pdfwritter.write(f)
print("----- Completed ----- ")

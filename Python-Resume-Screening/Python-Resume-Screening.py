import PyPDF2

# Getting File Location
file_location = input("Enter File Location:")
print("Getting File from ",file_location)

# Opening PDF File
pdf_file = open(file_location,'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# Getting Count of Number of Pages
num_of_pages = read_pdf.numPages

# Declaring variables for text in resume and number of resume pages processed

text_in_resume = ""
pages_processed = 0

while pages_processed < num_of_pages:
    pageObj = read_pdf.getPage(pages_processed)
    pages_processed +=1
    text_in_resume += pageObj.extractText()

pdf_file.close()

print(text_in_resu

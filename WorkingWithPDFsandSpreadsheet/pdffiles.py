import PyPDF2
f = open('Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)

print(len(pdf_reader.pages)) # output 5
page_one = pdf_reader.pages(0)
page_one_text = page_one.extractText()

print(page_one_text) # output pdf first page

f.close()

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)

first_page = pdf_reader.pages(0)

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.addPage(first_page)

pdf_output = open("Some_BrandNew_Doc.pdf", "wb")
pdf_writer.write(pdf_output)
f.close
pdf_output.close()

f = open('Working_Business_Proposal.pdf', 'rb')

pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):
    
    page = pdf_reader.pages(num)
    
    pdf_text.append(page.extractText())
    
print(pdf_text[1])

from PyPDF2 import PdfFileMerger

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

txtfile = open('/home/surya/Desktop/list.txt','rb')

pdfs=txtfile.read()

pdfs=pdfs.split('\n')

pdfs

merger = PdfFileMerger( strict=False)
for pdf in pdfs[:-1]:
    pdf=pdf.replace(" ", "")
    if pdf!='' :
        merger.append(open(pdf, 'rb'))

with open('lab_manuals.pdf', 'wb') as fout:
    merger.write(fout)
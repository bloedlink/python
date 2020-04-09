import PyPDF2
import os
import sys



watermark = sys.argv[1]
destination = sys.argv[2]
source = os.listdir()



if not os.path.exists(destination):
    os.mkdir(destination)


with open(watermark,'rb') as watermark_open:
    watermark_read = PyPDF2.PdfFileReader(watermark_open)

    watermark_pdf = watermark_read.getPage(0)

    for i in source:
        if i.endswith('.pdf'):
            with open(i,'rb') as source_open:
                source_read = PyPDF2.PdfFileReader(source_open)

                source_num = source_read.getNumPages() -1

                source_real = int(source_num)

                source_pdf = source_read.getPage(source_real)

                source_pdf.mergePage(watermark_pdf)

                writer = PyPDF2.PdfFileWriter()
                writer.addPage(source_pdf)
                with open(f'{destination}{i}','wb') as merger_file:
                    writer.write(merger_file)

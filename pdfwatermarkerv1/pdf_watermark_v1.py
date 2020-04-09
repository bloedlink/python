import PyPDF2
import os
import sys

watermark = sys.argv[1]
destination_file = sys.argv[2]
merged_file = 'finaltest.pdf'

def watermarker(watermark,destination_file):
    open_watermark = open(watermark, 'rb')
    watermark_reader = PyPDF2.PdfFileReader(open_watermark)


    open_destination = open(destination_file,'rb')
    destination_reader = PyPDF2.PdfFileReader(open_destination)

    watermark_page = watermark_reader.getPage(0)

    destination_page = destination_reader.getPage(0)

    watermark_page.mergePage(destination_page)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(watermark_page)

    merged_file = open('finaltest.pdf','wb')
    writer.write(merged_file)

    open_watermark.close()
    open_destination.close()
    merged_file.close()



watermarker(watermark, destination_file)

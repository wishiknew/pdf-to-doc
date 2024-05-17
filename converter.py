from pdf2docx import Converter
import fitz

pdf_file = 'LEASE DEED 15.04.2024.pdf'
docx_file = 'LEASE DEED 15.04.2024.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
import pdfkit
import os
# pdfkit.from_file('index.html','upload_to_s3/index.pdf')
# pdfkit.from_url('http://google.com', 'out.pdf')
x = input("Write a sentence/string which you'd like convert to PDF file.\n")
pdfkit.from_string(x, 'out.pdf')


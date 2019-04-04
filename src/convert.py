import pdfkit
import os
pdfkit.from_file('index.html','upload_to_s3/index.pdf')
# pdfkit.from_url('http://google.com', 'out.pdf')


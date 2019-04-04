import pdfkit
import os

# pdfkit.from_file('index.html','index.pdf')
# pdfkit.from_url('http://google.com', 'out.pdf')
# x = input("Write a sentence/string which you'd like convert to PDF file.\n")
# pdfkit.from_string(x, 'output.pdf')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output/')


def html_to_pdf():
    filename = input("What is the filename you want to convert?\n - ")
    pdfkit.from_file( INPUT_DIR+ '/' + filename+'.html', OUTPUT_DIR+"/index.pdf")

def string_to_pdf():
    string = input("What are the strings you want to convert?\n - ")
    pdfkit.from_string( string, OUTPUT_DIR +"/string.pdf")

def url_to_pdf():
    url_name = input("What is the url you want to convert?\n  ")
    pdfkit.from_url( url_name, OUTPUT_DIR+"/url_name.pdf")


print(" 1 : HTML\n 2 : String\n 3 : URL")
file_type = input("What type of file (extension) you wanna convert? - Choose one of the following:\n")


options = {
    1: html_to_pdf,
    2: string_to_pdf,
    3: url_to_pdf,
}


if __name__ == '__main__':
    options[int(file_type)]()


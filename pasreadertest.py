import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    ''' This part writes project names to a list without a chosen prefix'''
    i = 0
    slash_count = 0
    project = ''
    projects = []
    while i <= len(text):
        if text[i:i+4] == 'PREFIX-':
            secondary_iterator = 0
            for char in text[i+4:i+100]:
                project += char
                secondary_iterator += 1
                if char == '/':
                    slash_count += 1
                    if slash_count == 2:
                        project += text[i+4+secondary_iterator]
                        projects.append(project)
                        project = ''
                        break
        slash_count = 0
        i += 1

    '''This part writes project prices to a list in the same order as in project list'''
    price_list = []
    split_text = text.split('\n')
    for item in split_text:
        try:
            if type(float(item)) == float:
                price_list.append(float(item))
        except ValueError:
            pass
    price_list.pop()

    return projects, price_list

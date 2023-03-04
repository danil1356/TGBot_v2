from PyPDF2 import PdfFileReader


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(104)

        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)


path = 'Spring_v_deystvii_6_izd.pdf'
text_extractor(path)

from pdfminer.high_level import extract_text

text = extract_text("example.pdf")
print(text)


from pdfminer.high_level import extract_text

text = extract_text("Spring_v_deystvii_6_izd.pdf")
print(text)

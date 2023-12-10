import textract

def make_text(pdf):

    doc = textract.process(pdf)

    with open('temp.txt', 'w') as f:
        f.write(doc.decode('utf-8'))


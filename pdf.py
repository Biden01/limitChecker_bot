from PyPDF2 import PdfReader


def read_pdf(pdf_filename, filename):
    pdf = PdfReader(pdf_filename)
    page = pdf.pages[0]
    text = page.extractText()
    with open(f"temp/{filename}.txt", "w") as f:
        f.write(text)
    return text
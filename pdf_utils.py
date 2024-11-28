# pdf_utils.py
import fitz

def extract_pdf_text(pdf_file):
    """
    Extracts text from a PDF file passed in as a file-like object.
    """
    pdf_data = pdf_file.read()
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    page_data = ""
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_data += page.get_text()
    
    return page_data

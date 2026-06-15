import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    """
    Extract text from all pages of a PDF.
    """
    text_content = []

    try:
        doc = fitz.open(pdf_path)

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")

            text_content.append({
                "page_number": page_num + 1,
                "text": text
            })

        doc.close()

        return text_content

    except Exception as e:
        raise Exception(f"PDF Extraction Error: {str(e)}")
from utils.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text


class PDFProcessor:

    def process(pdf_path):

        pages = extract_text_from_pdf(pdf_path)

        full_text = ""

        for page in pages:
            cleaned_text = clean_text(page["text"])
            full_text += cleaned_text + "\n"

        return {
            "total_pages": len(pages),
            "content": full_text
        }
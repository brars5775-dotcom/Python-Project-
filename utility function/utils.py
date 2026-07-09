import fitz  # PyMuPDF
from pathlib import Path


class PDFUtils:
    """
    Utility functions for working with PDF files using PyMuPDF.
    """

    @staticmethod
    def open_pdf(pdf_path):
        """
        Open a PDF document.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            fitz.Document
        """
        if not Path(pdf_path).exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        return fitz.open(pdf_path)

    @staticmethod
    def get_page_count(pdf_path):
        """
        Returns the total number of pages.
        """
        with fitz.open(pdf_path) as doc:
            return len(doc)

    @staticmethod
    def extract_text(pdf_path):
        """
        Extract text from all pages.

        Returns:
            str
        """
        text = []

        with fitz.open(pdf_path) as doc:
            for page in doc:
                text.append(page.get_text("text"))

        return "\n".join(text)

    @staticmethod
    def extract_text_by_page(pdf_path):
        """
        Extract text page by page.

        Returns:
            list
        """
        pages = []

        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                pages.append({
                    "page": page_number,
                    "text": page.get_text("text")
                })

        return pages

    @staticmethod
    def extract_metadata(pdf_path):
        """
        Extract PDF metadata.

        Returns:
            dict
        """
        with fitz.open(pdf_path) as doc:
            return doc.metadata

    @staticmethod
    def search_text(pdf_path, keyword):
        """
        Search for a keyword in the PDF.

        Returns:
            list
        """
        matches = []

        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                if keyword.lower() in page.get_text().lower():
                    matches.append(page_number)

        return matches

    @staticmethod
    def extract_links(pdf_path):
        """
        Extract hyperlinks from the PDF.

        Returns:
            list
        """
        links = []

        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                for link in page.get_links():
                    links.append({
                        "page": page_number,
                        "link": link
                    })

        return links

    @staticmethod
    def extract_images(pdf_path):
        """
        Returns information about images in the PDF.

        Returns:
            list
        """
        images = []

        with fitz.open(pdf_path) as doc:
            for page_number, page in enumerate(doc, start=1):
                for img in page.get_images(full=True):
                    images.append({
                        "page": page_number,
                        "xref": img[0]
                    })

        return images
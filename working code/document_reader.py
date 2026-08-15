import os

from pypdf import PdfReader
from docx import Document


def extract_text(file_path):

    if not file_path:
        print("No file path provided.")
        return None

    if not os.path.exists(file_path):
        print("File does not exist.")
        return None

    extension = os.path.splitext(file_path)[1].lower()

    try:

        # PDF
        if extension == ".pdf":
            return extract_pdf(file_path)

        # DOCX
        elif extension == ".docx":
            return extract_docx(file_path)

        # TXT
        elif extension == ".txt":
            return extract_txt(file_path)

        else:
            print("Unsupported file type.")
            print("Supported formats: PDF, DOCX, TXT")
            return None

    except Exception as e:
        print(f"Document reading error: {e}")
        return None


def extract_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_docx(file_path):

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text.strip()


def extract_txt(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read().strip()
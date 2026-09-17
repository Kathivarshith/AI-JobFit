import re
import pymupdf


def extract_text_from_pdf(pdf_file):
    document = pymupdf.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text() + "\n"

    document.close()

    return text


def clean_text(text):
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n+",
        "\n",
        text
    )

    text = text.strip()

    return text
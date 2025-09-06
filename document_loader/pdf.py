"""
This module provides a function to load a PDF document and return a LangChain Document object.
"""

from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document


def load_pdf(file_path: str) -> Document:
    """
    Loads a PDF file and returns a LangChain Document object.

    Args:
        file_path: The path to the PDF file.

    Returns:
        A LangChain Document object containing the content of the PDF.
    """
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return pages


if __name__ == "__main__":
    # Example usage
    pdf_path = "../docs/pdf/agentic-ai.pdf"  # Replace with your PDF file path
    documents = load_pdf(pdf_path)
    for i, doc in enumerate(documents):
        print(f"Page {i + 1}:\n{doc.page_content}\n")

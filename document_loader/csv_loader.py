"""This module implements a CSV document loader using LangChain."""

from langchain_community.document_loaders.csv_loader import CSVLoader


def load_csv(file_path: str):
    """
    Loads a CSV file and returns its content as a list of documents.

    Args:
        file_path: The path to the CSV file.

    Returns:
        A list of documents, where each document represents a row in the CSV.
    """
    loader = CSVLoader(file_path=file_path)
    return loader.load()


if __name__ == "__main__":
    # Example usage
    file_path = "../docs/csv/employee-data.csv"
    documents = load_csv(file_path)
    for doc in documents:
        print(doc)

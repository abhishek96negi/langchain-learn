# Langchain PDF Loader

This project is a Python application that demonstrates how to load and process PDF documents using the LangChain framework. It provides a simple and effective way to extract text from PDF files, splitting them into individual pages for further processing.

## Installation

To get started with this project, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/langchain-learn.git
    cd langchain-learn
    ```

2.  **Create and activate the virtual environment:**

    Use `uv` to create a virtual environment:
    ```bash
    uv venv
    ```

    Activate the virtual environment. On macOS and Linux, run:
    ```bash
    source .venv/bin/activate
    ```

    On Windows, use:
    ```bash
    .venv\Scripts\activate
    ```

3.  **Install the dependencies:**

    The required dependencies are listed in the `requirements.txt` file. You can install them using `uv`:

    ```bash
    uv add -r requirements.txt
    ```

    The dependencies include:
    *   `langchain`
    *   `langchain-core`
    *   `langchain-community`
    *   `pypdf`

## Usage

The main functionality of this project is to load a PDF file and extract its content. You can see an example of how to use the `load_pdf` function in the `document_loader/pdf.py` file.

To run the example, you can execute the `pdf.py` script directly:

```bash
python document_loader/pdf.py
```

This will load the PDF file located at `docs/pdf/agentic-ai.pdf`, split it into pages, and print the content of each page to the console.

You can easily modify the `pdf.py` script to load your own PDF files by changing the `pdf_path` variable.

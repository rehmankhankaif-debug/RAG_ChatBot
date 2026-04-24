from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    docs = splitter.split_documents(documents)

    # Note: Returning `docs` directly, NOT `doc.page_content`.
    # FAISS requires LangChain Document objects.
    return docs

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def create_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore


def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 5,
            "score_threshold": 0.04,
        },
    )

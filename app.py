import streamlit as st
from pdf_loader import load_pdf
from vectorstore import create_vectorstore, get_retriever
from rag_chain import build_rag_chain

st.title("📄 RAG Chatbot (PDF)")

pdf_path = "/Users/kaifrehmankhan/Desktop/Advanced_Multimodel_RAG_2.0/data/Transformers.pdf"


@st.cache_resource
def setup_rag():
    docs = load_pdf(pdf_path)
    vectorstore = create_vectorstore(docs)
    retriever = get_retriever(vectorstore)
    rag_chain = build_rag_chain(retriever)
    return rag_chain


rag = setup_rag()

question = st.text_input("Ask a question:")

if question:
    answer = rag(question)
    st.write("### Answer")
    st.write(answer)

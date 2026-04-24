from pdf_loader import load_pdf
from vectorstore import create_vectorstore, get_retriever
from rag_chain import build_rag_chain

print("🚀 Loading PDF RAG system...")

pdf_path = (
    "/Users/kaifrehmankhan/Desktop/Advanced_Multimodel_RAG_2.0/data/Transformers.pdf"
)
docs = load_pdf(pdf_path)
db = create_vectorstore(docs)
retriever = get_retriever(db)

rag_chain = build_rag_chain(retriever)

print("✅ Ready!\n")

while True:
    query = input("You: ")

    if query.lower() in ["exit", "quit"]:
        break

    result = rag_chain(query)

    print("\n🤖 Answer:\n")
    print(result)

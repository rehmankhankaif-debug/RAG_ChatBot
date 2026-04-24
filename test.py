from vectorstore import create_vectorstore
from pdf_loader import load_pdf

print("📄 PDF Load ho rahi hai...")
docs = load_pdf(
    "/Users/kaifrehmankhan/Desktop/Advanced_Multimodel_RAG/data/Transformers.pdf"
)

print(f"✅ Total chunks bane: {len(docs)}")

if len(docs) == 0:
    print(
        "🚨 ERROR: PDF se koi text read nahi hua! (Shayad yeh ek image/scanned PDF hai)"
    )
else:
    print("🧠 Vector Database ban raha hai...")
    db = create_vectorstore(docs)

    query = "what is transformers"
    print(f"\n🔍 Searching for: '{query}'")

    # Yeh asli similarity score batayega jo FAISS calculate kar raha hai
    results = db.similarity_search_with_relevance_scores(query, k=8)

    if not results:
        print("🚨 Koi matching result nahi mila!")

    for i, (doc, score) in enumerate(results):
        print(f"\n--- Result {i+1} ---")
        print(f"🎯 Score: {score}")
        print(f"📝 Text: {doc.page_content[:200]}...")

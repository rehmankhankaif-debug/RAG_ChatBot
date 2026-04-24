from transformers import pipeline


def format_docs(docs, max_chars=3000):
    """Convert Document objects into limited clean text"""
    cleaned_docs = []
    for doc in docs[:4]:
        text = doc.page_content.strip()
        cleaned_docs.append(text[:1000])

    context = "\n\n".join(cleaned_docs)
    return context[:max_chars]


def format_prompt(context, question):
    return f"""<|system|>
You are a helpful AI assistant.

RULES:
- Answer ONLY using the provided context
- If answer is not present → say "I don't know"
- Give a detailed, well-structured explanation
- Use paragraphs and bullet points when needed
- Do NOT stop mid-sentence

</s>
<|user|>
Context:
{context}

Question:
{question}

Give a detailed answer:
</s>
<|assistant|>
"""


def build_rag_chain(retriever):
    """Build RAG pipeline with TinyLlama"""
    pipe = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        max_new_tokens=500,
        temperature=0.3,
        do_sample=True,
        return_full_text=False,
    )

    def rag_pipeline(question):
        docs = retriever.invoke(question)

        if not docs:
            return "I don't know"

        context = format_docs(docs)
        prompt = format_prompt(context, question)

        response = pipe(prompt, truncation=True)
        answer = response[0]["generated_text"].strip()

        if not answer:
            return "I don't know"

        return answer

    return rag_pipeline

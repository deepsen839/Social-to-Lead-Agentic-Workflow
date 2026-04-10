import json
import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.embeddings import FakeEmbeddings
from langchain_groq import ChatGroq
import os
load_dotenv()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)
def load_vectorstore():
    with open("data/knowledge_base.json") as f:
        kb = json.load(f)

    docs = []
    for key, value in kb.items():
        docs.append(Document(page_content=f"{key}: {value}"))

    embeddings = FakeEmbeddings(size=384)

    return FAISS.from_documents(docs, embeddings)

vectorstore = load_vectorstore()

def rag_node(state):
    query = state["user_input"]

    if "price" in query.lower() or "plan" in query.lower():
        docs = vectorstore.similarity_search("", k=10)  # get all pricing info
    else:
        docs = vectorstore.similarity_search(query, k=2)

    context = "\n".join([d.page_content for d in docs])
    answer = llm.invoke(f"""
            You are AutoStream AI.

            Format response clearly:

            - Use bullet points
            - Keep it short
            - NO markdown (**)
            - NO extra features

            Context:
            {context}

            Question: {query}
            """).content
    

    return {"response": answer}
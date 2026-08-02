from rag.retriever import retrieve
from llm.prompts import RAG_PROMPT
from llm.llm import llm
from llm.output_parser import get_content


question = "What is Dow Jones?"

results = retrieve(question)

context = "\n\n".join(
    results["documents"][0]
)

messages = [
    {
        "role":"system",
        "content":
        RAG_PROMPT
        +
        f"\n\nContext:\n{context}"
    },
    {
        "role":"user",
        "content":question
    }
]

response = llm.chat(messages)

print(get_content(response))
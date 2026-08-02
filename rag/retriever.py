from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


embedder = EmbeddingModel()

vector_db = VectorStore()


def retrieve(
    question: str,
    top_k: int = 5
):

    embedding = embedder.embed_text(question)

    results = vector_db.search(
        embedding,
        top_k=top_k
    )

    return results
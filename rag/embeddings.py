from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingModel:

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5"
    ):

        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> List[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_documents(
        self,
        documents: List[str]
    ) -> List[List[float]]:

        embeddings = self.model.encode(
            documents,
            normalize_embeddings=True
        )

        return embeddings.tolist()
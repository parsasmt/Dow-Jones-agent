import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="dow_jones"
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
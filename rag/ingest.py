from pathlib import Path

from rag.chunking import TextChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


chunker = TextChunker()

embedder = EmbeddingModel()

vector_db = VectorStore()


def ingest_directory(directory: str):

    directory = Path(directory)

    txt_files = list(directory.rglob("*.txt"))
    md_files = list(directory.rglob("*.md"))

    files = txt_files + md_files

    counter = 0

    for file in files:

        text = file.read_text(encoding="utf-8")

        chunks = chunker.split_text(text)

        embeddings = embedder.embed_documents(chunks)

        ids = []
        metadata = []

        for i, chunk in enumerate(chunks):

            ids.append(f"{file.stem}_{i}")

            metadata.append({
                "source": str(file),
                "chunk": i
            })

        vector_db.add_documents(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadata
        )

        counter += len(chunks)

    print(f"Ingested {counter} chunks.")
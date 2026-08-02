from rag.retriever import retrieve

if __name__ == "__main__":

    results = retrieve(
        "What is Dow Jones?"
    )

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

for i, doc in enumerate(documents):

    print("=" * 80)

    print(f"Chunk {i+1}")

    print(metadata[i])

    print()

    print(doc)

    print()
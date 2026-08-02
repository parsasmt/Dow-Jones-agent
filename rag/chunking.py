from typing import List


class TextChunker:
    """
    Splits text into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks.

        Args:
            text: Input text

        Returns:
            List of chunks
        """

        if not text:
            return []

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.chunk_overlap

        return chunks
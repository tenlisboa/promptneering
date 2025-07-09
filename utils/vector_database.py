from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

class VectorDB:
    def __init__(self, name: str):
        client = PersistentClient()
        embedding = SentenceTransformerEmbeddingFunction()
        self.collection = client.get_collection(name, embedding_function=embedding)

    def query(self, query_texts, n_results=10) -> list[str]:
        return self.collection.query(query_texts=query_texts, n_results=n_results)['documents']

    def add(self, documents):
        self.collection.add(documents)

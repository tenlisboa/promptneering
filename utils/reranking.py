from sentence_transformers import CrossEncoder

class ReRanking():
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, documents: list[str]) -> list[tuple[str, float]]:
        scores = self.model.predict([(query, doc) for doc in documents])
        return sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)

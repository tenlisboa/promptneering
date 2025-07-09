from langchain_core.tools import tool
from utils.expander import Expander
from utils.reranking import ReRanking
from utils.vector_database import VectorDB

db = VectorDB('prompt_engineering_knowledge')

@tool()
def knowledge_tool(query: str):
    """ Consult prompt engineering knowledge

    Args:
        query: User request
    """
    expander = Expander()
    queries = expander.expand(query)

    results = db.query(query_texts=queries, n_results=10)

    retrieved_documents = set()
    for documents in results:
        for document in documents:
            retrieved_documents.add(document)

    reranked_documents = ReRanking().rerank(query, list(retrieved_documents))

    top_five = reranked_documents[:5]

    return '\n\n'.join([r[0] for r in top_five])

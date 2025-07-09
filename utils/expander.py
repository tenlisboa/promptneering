from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from prompts import load

class Expander:
    def __init__(self):
        self.llm = ChatOpenAI(
            model='gpt-3.5-turbo',
            temperature=0.7
        )

    def expand(self, query: str) -> list[str]:
        system = SystemMessage(
            content=load('expand_query')
        )
        user = HumanMessage(content=f"Create five questions from: {query}")
        result = self.llm.invoke([
            system,
            user
        ])

        return [q.strip() for q in result.content.split('\n\n')]  

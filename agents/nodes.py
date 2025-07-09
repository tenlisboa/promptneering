from prompts import load
from agents.agents import State
from langchain_core.messages import SystemMessage 
from langchain_openai import ChatOpenAI

class Assistant:
    def __init__(self, tools=None):
        llm =ChatOpenAI(
            model='gpt-4o-mini',
            temperature=0.0
        )

        self.llm = llm.bind_tools(tools) if tools else llm

    def invoke(self, state: State) -> dict:
        system = SystemMessage(
            content=load('assistant')
        )

        return {"messages": [self.llm.invoke([system] + state['messages'])]}

from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict
from typing import Annotated 
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import InMemorySaver
from agents.nodes import Assistant

class State(TypedDict):
    query: Annotated[str, lambda x: x.strip()]
    messages: Annotated[list[BaseMessage], add_messages]

class Agent:
    def __init__(self, tools=None):
        self.builder = StateGraph(State)
        self.tools = tools

    def compile(self) -> CompiledStateGraph:
        self.builder.add_node('assistant', Assistant(self.tools).invoke)
        self.builder.add_node('tools', ToolNode(self.tools))

        self.builder.add_edge(START, 'assistant')
        self.builder.add_conditional_edges(
            'assistant',
            tools_condition
        )
        self.builder.add_edge('tools', 'assistant')

        checkpointer = InMemorySaver()
        return self.builder.compile(checkpointer=checkpointer)

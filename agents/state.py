from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    query: str
    messages: Annotated[list[BaseMessage], add_messages]

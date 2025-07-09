import gradio as gr
from agents.agents import Agent
from langchain_core.messages import HumanMessage
from tools.knowledge import knowledge_tool

agent = Agent([knowledge_tool])
compiled_graph = agent.compile()

def gradio_chat(query):
    messages = [HumanMessage(content=query)]
    config = {'thread_id': "gradio"}
    response = compiled_graph.invoke({"messages": messages, "query": query}, {'configurable': config})
    for m in reversed(response['messages']):
        if not isinstance(m, HumanMessage) and hasattr(m, 'content'):
            return m.content
    return "No response."

iface = gr.Interface(
    fn=gradio_chat,
    inputs=gr.Textbox(lines=2, label="Your question"),
    outputs=gr.Textbox(label="Assistant"),
    title="Prompt Engineering Assistant"
)

if __name__ == "__main__":
    iface.launch()

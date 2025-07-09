from agents.agents import Agent
from langchain_core.messages import HumanMessage

def main():
    agent = Agent([])
    compiled_graph = agent.compile()

    query = "Create a simple prompt for a chatbot."
    state = {
        "query": query,
        "messages": [
            HumanMessage(content=query)
        ]
    }

    config = {
        "configurable": {
            "thread_id": "12345",
        }         
    }
    
    response = compiled_graph.invoke(state, config)
    for m in response['messages']:
        m.pretty_print()

if __name__ == "__main__":
    main()

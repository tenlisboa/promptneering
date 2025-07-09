from agents.agents import Agent

def main():
    agent = Agent()
    compiled_graph = agent.compile()

    state = {
        "query": "Create a simple prompt for a chatbot.",
        "messages": []
    }

    result = compiled_graph.invoke(state)
    print(result)

if __name__ == "__main__":
    main()

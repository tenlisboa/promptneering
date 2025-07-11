# Promptneering

Promptneering is a prompt engineering assistant that leverages LLMs, vector databases, and agent-based architectures to provide context-aware answers and prompt engineering support.

## Technologies and Strategies

- **LLM Integration:** Uses OpenAI's GPT-4o-mini and GPT-3.5-turbo via LangChain for prompt expansion, answering, and tool binding.
- **Vector Database:** Employs ChromaDB for persistent storage and retrieval of prompt engineering knowledge, with semantic search and re-ranking using Sentence Transformers and CrossEncoder.
- **Agent Architecture:** Implements a modular agent system using LangGraph, with nodes for assistant logic and tool invocation. Agents use a state graph to manage conversation flow and tool usage.
- **Prompt Expansion:** Automatically expands user queries into multiple related questions to improve retrieval and context coverage.
- **Re-ranking:** Retrieved documents are re-ranked for relevance using a cross-encoder model.
- **Gradio UI:** Provides a simple web interface for user interaction.

## Project Structure

- `main.py` / `main.ipynb`: Entry points for running the assistant (script or notebook).
- `agents/`: Agent logic, state management, and node definitions.
- `tools/`: Tool definitions, including knowledge retrieval.
- `utils/`: Utilities for prompt expansion, re-ranking, and vector database operations.
- `documents/`: Knowledge base in markdown format.
- `prompts/`: Prompt templates for system and tool instructions.
- `chroma/`: Vector database storage.

## Setup and Running

1. **Environment Setup**

   - Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).
   - Create the environment:
     ```sh
     conda env create -f environment.yml
     conda activate promptneering
     ```

2. **Run the Assistant**

   - To launch the Gradio web interface:
     ```sh
     python main.py
     ```
   - Or use the Jupyter notebook for step-by-step exploration:
     ```sh
     jupyter notebook main.ipynb
     ```

3. **Configuration**
   - Place your OpenAI API key and other secrets in a `.env` file in the project root.

## Notes

- The vector database is pre-populated from the `documents/` directory. To update, use the provided notebooks in `notebooks/`.
- The agent architecture is extensible; new tools and nodes can be added in the `tools/` and `agents/` directories.

## References

- [LangChain](https://python.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Gradio](https://gradio.app/)
- [Sentence Transformers](https://www.sbert.net/)

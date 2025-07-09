def load(name: str):
    """
    Load a prompt from the prompts directory.
    
    Args:
        name (str): The name of the prompt to load.
        
    Returns:
        str: The content of the prompt.
    """
    with open(f"prompts/{name}.md", "r") as file:
        return file.read()

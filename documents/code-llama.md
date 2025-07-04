# Prompting Guide for Code Llama


Code Llama is a family of large language models (LLM), released by Meta, with the capabilities to accept text prompts and generate and discuss code. The release also includes two other variants (Code Llama Python and Code Llama Instruct) and different sizes (7B, 13B, 34B, and 70B).

In this prompting guide, we will explore the capabilities of Code Llama and how to effectively prompt it to accomplish tasks such as code completion and debugging code. 

We will be using the Code Llama 70B Instruct hosted by together.ai for the code examples but you can use any LLM provider of your choice. Requests might differ based on the LLM provider but the prompt examples should be easy to adopt.  

For all the prompt examples below, we will be using [Code Llama 70B Instruct](https://about.fb.com/news/2023/08/code-llama-ai-for-coding/), which is a fine-tuned variant of Code Llama that's been instruction tuned to accept natural language instructions as input and produce helpful and safe answers in natural language. You might get very different responses from the model so the outputs we demonstrate here might be difficult to reproduce. In general, the prompts provided should produce satisfactory responses; when this is not the case, you may need to tune the prompts a bit more to get the desired results.

## Table of Contents

- [Configure Model Access](#configure-model-access)
- [Basic Code Completion](#basic-code-completion)
- [Debugging](#debugging)
- [Unit Tests](#unit-tests)
- [Text-to-SQL Generation](#text-to-sql-generation)
- [Few-shot Prompting with Code Llama](#few-shot-prompting-with-code-llama)
- [Function Calling](#function-calling)
- [Safety Guardrails](#safety-guardrails)
- [Notebook](#full-notebook)
- [References](#additional-references)

## Configure Model Access

The first step is to configure model access. Let's install the following libraries to get started:

```python
%%capture
!pip install openai
!pip install pandas
```

Let's import the necessary libraries and set the `TOGETHER_API_KEY` which you you can obtain at [together.ai](https://api.together.xyz/). We then set the `base_url` as `https://api.together.xyz/v1` which will allow us to use the familiar OpenAI python client.

```python
import openai
import os
import json
from dotenv import load_dotenv
load_dotenv()

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

client = openai.OpenAI(
    api_key=TOGETHER_API_KEY,
    base_url="https://api.together.xyz/v1",
)
```

Let's define a completion function that we can call easily with different prompt examples:

```python
def get_code_completion(messages, max_tokens=512, model="codellama/CodeLlama-70b-Instruct-hf"):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        max_tokens=max_tokens,
        stop=[
            ""
        ],
        frequency_penalty=1,
        presence_penalty=1,
        top_p=0.7,
        n=10,
        temperature=0.7,
    )

    return chat_completion
```

## Basic Code Completion

Let's test out a basic example where we ask the model to generate a valid Python function that can generate the nth fibonnaci number.

```python
messages = [
      {
            "role": "system",
            "content": "You are an expert programmer that helps to write Python code based on the user request, with concise explanations. Don't be too verbose.",
      },
      {
            "role": "user",
            "content": "Write a python function to generate the nth fibonacci number.",
      }
]

chat_completion = get_code_completion(messages)
            
print(chat_completion.choices[0].message.content)
```

Output (truncated for brevity):

```
Here is a simple Python function to generate the nth Fibonacci number:


def generate_fibonacci(n):
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1

    # Recursive call to generate the nth Fibonacci number
    return generate_fibonacci(n-1) + generate_fibonacci(n-2)

In this function, we use recursion to generate the nth Fibonacci number. The base cases are when n is 1 or 2, in which case we return 0 and 1 respectively. For all other values of n, we recursively call the function to generate the (n-1)th and (n-2)th Fibonacci numbers and add them together to get the nth Fibonacci number...
```

## Debugging
We can use the model to help debug a piece of code. Let's say we want to get feedback from the model on a piece of code we wrote to check for bugs. Here is an example demonstrating this capability:

```python
messages = [
    {
        "role": "system",
        "content": "You are an expert programmer that helps to review Python code for bugs."
    },
    {
    "role": "user",
    "content": """Where is the bug in this code?

    def fib(n):
        if n >> [h(2) for h in power_funcs(3)]
[2, 4, 8]
```

## Unit Tests

The model can also be used to write unit tests. Here is an example:

```python
prompt = """
[INST] Your task is to write 2 tests to check the correctness of a function that solves a programming problem.
The tests must be between [TESTS] and [/TESTS] tags.
You must write the comment "#Test case n:" on a separate line directly above each assert statement, where n represents the test case number, starting from 1 and increasing by one for each subsequent test case.

Problem: Write a Python function to get the unique elements of a list.
[/INST]
"""

messages = [
    {
        "role": "system",
        "content": "You are an expert programmer that helps write unit tests. Don't explain anything just write the tests.",
    },
    {
        "role": "user",
        "content": prompt,
    }
]

chat_completion = get_code_completion(messages)
            
print(chat_completion.choices[0].message.content)
```

Output:

```
[TESTS]
# Test case 1:
assert get_unique_elements([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], f"Expected get_unique_elements([1, 2, 3, 4, 5]) to return [1, 2, 3, 4, 5], but got {get_unique_elements([1, 2, 3, 4, 5])}"

# Test case 2:
assert get_unique_elements([1, 1, 2, 2, 3, 3]) == [1, 2, 3], f"Expected get_unique_elements([1, 1, 2, 2, 3, 3]) to return [1, 2, 3], but got {get_unique_elements([1, 1, 2, 2, 3, 3])}"
[/TESTS]
```

The example above was adopted from the [the official Code Llama paper](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/). 

## Text-to-SQL Generation

The prompt below also tests for Text-to-SQL capabilities where we provide information about a database schema and instruct the model to generate a valid query.

```python
prompt = """
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
""""""

"""

messages = [
    {
        "role": "user",
        "content": prompt,
    }
]

chat_completion = get_code_completion(messages)
            
print(chat_completion.choices[0].message.content)
```

```
SELECT s.StudentId, s.StudentName
FROM students s
INNER JOIN departments d ON s.DepartmentId = d.DepartmentId
WHERE d.DepartmentName = 'Computer Science';
```

## Few-shot Prompting with Code Llama

We can leverage few-shot prompting for performing more complex tasks with Code Llama 70B Instruct. Let's first create a pandas dataframe that we can use to evaluate the responses from the model.

```python
import pandas as pd

# Sample data for 10 students
data = {
    "Name": ["Alice Johnson", "Bob Smith", "Carlos Diaz", "Diana Chen", "Ethan Clark",
             "Fiona O'Reilly", "George Kumar", "Hannah Ali", "Ivan Petrov", "Julia Müller"],
    "Nationality": ["USA", "USA", "Mexico", "China", "USA", "Ireland", "India", "Egypt", "Russia", "Germany"],
    "Overall Grade": ["A", "B", "B+", "A-", "C", "A", "B-", "A-", "C+", "B"],
    "Age": [20, 21, 22, 20, 19, 21, 23, 20, 22, 21],
    "Major": ["Computer Science", "Biology", "Mathematics", "Physics", "Economics",
              "Engineering", "Medicine", "Law", "History", "Art"],
    "GPA": [3.8, 3.2, 3.5, 3.7, 2.9, 3.9, 3.1, 3.6, 2.8, 3.4]
}

# Creating the DataFrame
students_df = pd.DataFrame(data)
```

We can now create our few-shot demonstrations along with the actual prompt (`FEW_SHOT_PROMPT_USER`) that contains the user's question we would like the model to generate valid pandas code for. 

```python
FEW_SHOT_PROMPT_1 = """
You are given a Pandas dataframe named students_df:
- Columns: ['Name', 'Nationality', 'Overall Grade', 'Age', 'Major', 'GPA']
User's Question: How to find the youngest student?
"""
FEW_SHOT_ANSWER_1 = """
result = students_df[students_df['Age'] == students_df['Age'].min()]
"""

FEW_SHOT_PROMPT_2 = """
You are given a Pandas dataframe named students_df:
- Columns: ['Name', 'Nationality', 'Overall Grade', 'Age', 'Major', 'GPA']
User's Question: What are the number of unique majors?
"""
FEW_SHOT_ANSWER_2 = """
result = students_df['Major'].nunique()
"""

FEW_SHOT_PROMPT_USER = """
You are given a Pandas dataframe named students_df:
- Columns: ['Name', 'Nationality', 'Overall Grade', 'Age', 'Major', 'GPA']
User's Question: How to find the students with GPAs between 3.5 and 3.8?
"""
```

Finally, here is the final system prompt, few-shot demonstrations, and final user question:

```python
messages = [
    {
        "role": "system",
        "content": "Write Pandas code to get the answer to the user's question. Store the answer in a variable named `result`. Don't include imports. Please wrap your code answer using ```."
    },
    {
        "role": "user",
        "content": FEW_SHOT_PROMPT_1
    },
    {
        "role": "assistant",
        "content": FEW_SHOT_ANSWER_1
    },
    {
        "role": "user",
        "content": FEW_SHOT_PROMPT_2
    },
    {
        "role": "assistant",
        "content": FEW_SHOT_ANSWER_2
    },
    {
        "role": "user",
        "content": FEW_SHOT_PROMPT_USER
    }
]

chat_completion = get_code_completion(messages)
            
print(chat_completion.choices[0].message.content)
```

Output:

```python
result = students_df[(students_df['GPA'] >= 3.5) & (students_df['GPA'] 
    }
    title="Prompting Guide for Code Llama"
    href="https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-code-llama.ipynb"
    />



## Additional References

- [together.ai Docs](https://docs.together.ai/docs/quickstart)
- [Code Llama - Instruct](https://about.fb.com/news/2023/08/code-llama-ai-for-coding/)
- [Code Llama: Open Foundation Models for Code](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/)
- [How to prompt Code Llama](https://ollama.ai/blog/how-to-prompt-code-llama)
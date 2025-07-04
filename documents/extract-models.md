# Extract Model Names from Papers


## Background
The following prompt tests an LLM's capabilities to perform an information extraction task which involves extracting model names from machine learning paper abstracts.

## Prompt

```markdown
Your task is to extract model names from machine learning paper abstracts. Your response is an array of the model names in the format [\"model_name\"]. If you don't find model names in the abstract or you are not sure, return [\"NA\"]

Abstract: Large Language Models (LLMs), such as ChatGPT and GPT-4, have revolutionized natural language processing research and demonstrated potential in Artificial General Intelligence (AGI). However, the expensive training and deployment of LLMs present challenges to transparent and open academic research. To address these issues, this project open-sources the Chinese LLaMA and Alpaca…
```

## Prompt Template

```markdown
Your task is to extract model names from machine learning paper abstracts. Your response is an array of the model names in the format [\"model_name\"]. If you don't find model names in the abstract or you are not sure, return [\"NA\"]

Abstract: {input}
```

## Code / API



## Reference
- [Prompt Engineering Guide](https://www.promptingguide.ai/introduction/examples#information-extraction) (16 March 2023)
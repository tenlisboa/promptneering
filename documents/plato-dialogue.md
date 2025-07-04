# Evaluate Plato's Dialogue


## Background
The following prompt tests an LLM's ability to perform evaluation on the outputs of two different models as if it was a teacher.

First, two models (e.g., ChatGPT & GPT-4) are prompted to using the following prompt:

```
Plato’s Gorgias is a critique of rhetoric and sophistic oratory, where he makes the point that not only is it not a proper form of art, but the use of rhetoric and oratory can often be harmful and malicious. Can you write a dialogue by Plato where instead he criticizes the use of autoregressive language models?
```

Then, those outputs are evaluated using the evaluation prompt below.

## Prompt
```
Can you compare the two outputs below as if you were a teacher?

Output from ChatGPT: {output 1}

Output from GPT-4: {output 2}
```

## Code / API



## Reference
- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
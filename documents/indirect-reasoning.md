# Indirect Reasoning with LLMs 


## Background
[Zhang et al. (2024)](https://arxiv.org/abs/2402.03667) recently proposed an indirect reasoning method to strengthen the reasoning power of LLMs. It employs the logic of contrapositives and contradictions to tackle IR tasks such as factual reasoning and mathematic proof. It consists of two key steps: 1) enhance the comprehensibility of LLMs by augmenting data and rules (i.e., logical equivalence of contrapositive), and 2) design prompt templates to stimulate LLMs to implement indirect reasoning based on proof by contradiction.

Experiments on LLMs like GPT-3.5-turbo and Gemini-pro show that the proposed method enhances the overall accuracy of factual reasoning by 27.33% and mathematic proof by 31.43% compared to traditional direct reasoning methods.

Below is an example of zero-shot template for proof-by-contradiction.


## Prompt
```
If a+|a|=0, try to prove that a
    

    




## Reference
- [Large Language Models as an Indirect Reasoner: Contrapositive and Contradiction for Automated Reasoning](https://arxiv.org/abs/2402.03667) (06 February 2024)
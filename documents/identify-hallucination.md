# Identify Hallucination in LLM Responses


## Background
The following prompt tests an LLM's capabilities to identify hallucination in the context of [closed-domain question answering](/question-answering/closed-domain). Bubeck et al. (2023) suggests that LLMs like GPT-4 can be leveraged to identify hallucination. 



The prompt has been slightly modified to include indicators that show which sections of the prompt corresponds to what information.

## Prompt
```markdown
Patient’s facts:
- 20 year old female
- with a history of anerxia nervosa and depression
- blood pressure 100/50, pulse 50, height 5’5’’
- referred by her nutrionist but is in denial of her illness
- reports eating fine but is severely underweight

Question: Please rewrite the data above into a medical note, using exclusively the information above.

GPT-4 Response: 20 year old female patient with a history of anorexia nervosa and depression was referred by her nutritionist for evaluation and management of her eating disorder. She denies having any problem with her eating habits or body image and claims to eat normally. However, she is severely underweight for her height (BMI 16.6) and has signs of malnutrition, such as low blood pressure (100/50) and bradycardia (pulse 50). She also reports feeling depressed and hopeless. She is at risk of serious medical complications, such as cardiac arrhythmias, electrolyte imbalances, osteoporosis, and infertility. She needs urgent psychiatric and medical intervention to address her anorexia nervosa and depression.

Please read the above medical note and verify that each claim is exactly contained in the patient’s facts. Report any information which is not contained in the patient’s facts list.
```

## Code / API



## Reference
- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
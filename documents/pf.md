The document discusses the concept of encapsulating prompts into functions for more efficient interaction with GPT, likening it to a programming language's shell. By defining a function with a unique name and specific input and rules, users can automate tasks and streamline workflows. An example of a function is `trans_word`, which translates text from Chinese to English, defined with the prompt: 
```
function_name: [trans_word]
input: ["text"]
rule: [I want you to act as an English translator, spelling corrector and improver...]
```
Other functions include `expand_word` for text expansion and `fix_english` for correcting text. Users can also create functions with multiple parameters, such as a password generator function `pg`. The document highlights various projects that enhance GPT's programming capabilities, suggesting that average users can utilize simple templates for daily tasks and explore open-source tools for further development.
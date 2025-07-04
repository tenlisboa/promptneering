# Draw a Person Using Alphabet Letters


## Background
The following prompt tests an LLM's capabilities to handle visual concepts, despite being trained only on text. This is a challenging task for the LLM so it involves several iterations. In the example below the user first requests for a desired visual and then provides feedback along with corrections and additions. The follow up instructions will depend on the progress the LLM makes on the task. Note that this task is asking to generate TikZ code which will then need to manually compiled by the user.

## Prompt

Prompt Iteration 1:
```markdown
Produce TikZ code that draws a person composed from letters in the alphabet. The arms and torso can be the letter Y, the face can be the letter O (add some facial features) and the legs can be the legs of the letter H. Feel free to add other features.
```  

Prompt Iteration 2:
```markdown
The torso is a bit too long, the arms are too short and it looks like the right arm is carrying the face instead of the face being right above the torso. Could you correct this please?
```

Prompt Iteration 3:
```markdown
Please add a shirt and pants.
```

## Code / API



## Reference
- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712) (13 April 2023)
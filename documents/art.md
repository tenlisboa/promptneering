# Automatic Reasoning and Tool-use (ART)


Combining CoT prompting and tools in an interleaved manner has shown to be a strong and robust approach to address many tasks with LLMs. These approaches typically require hand-crafting task-specific demonstrations and carefully scripted interleaving of model generations with tool use. [Paranjape et al., (2023)](https://arxiv.org/abs/2303.09014) propose a new framework that uses a frozen LLM to automatically generate intermediate reasoning steps as a program.

ART works as follows:
- given a new task, it select demonstrations of multi-step reasoning and tool use from a task library 
- at test time, it pauses generation whenever external tools are called, and integrate their output before resuming generation

ART encourages the model to generalize from demonstrations to decompose a new task and
use tools in appropriate places, in a zero-shot fashion. In addition, ART is extensible as it also enables humans to fix mistakes in the reasoning steps or add new tools by simply updating the task and tool libraries. The process is demonstrated below:


Image Source: [Paranjape et al., (2023)](https://arxiv.org/abs/2303.09014)

ART substantially improves over few-shot prompting and automatic CoT on unseen tasks in the BigBench and MMLU benchmarks, and exceeds performance of hand-crafted CoT prompts when human feedback is incorporated. 

Below is a table demonstrating ART's performance on BigBench and MMLU tasks:


Image Source: [Paranjape et al., (2023)](https://arxiv.org/abs/2303.09014)



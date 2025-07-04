# Produce MySQL Queries using LLMs


## Background
This prompt tests an LLM's code generation capabilities by prompting it to generate a valid MySQL query by providing information about the database schema.

## Prompt
```markdown
"""
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
"""
```

## Code / API




## Reference
- [Prompt Engineering Guide](https://www.promptingguide.ai/introduction/examples#code-generation) (16 March 2023)
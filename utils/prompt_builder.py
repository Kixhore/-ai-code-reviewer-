class PromptBuilder:
    """Utility class for building code review prompts"""
    
    def __init__(self):
        self.base_prompt = self._get_base_prompt()
    
    def _get_base_prompt(self) -> str:
        """Get the base prompt template"""
        return """You are a professional Python code reviewer with extensive experience in software development, code quality, and best practices.

Your task is to provide a comprehensive code review for the given problem statement and Python solution.

First, analyze whether the solution code matches the problem statement. If the solution doesn't address the problem correctly, highlight this as a major issue in your review.

Second, assess how much of the code appears to be human-written versus AI-generated. Provide a percentage estimate (e.g., "70% likely human-written, 30% likely AI-generated") and explain your reasoning based on code patterns, style consistency, and complexity.

Then, analyze the code based on the following criteria:

1. **Problem-Solution Match**
   - Does the solution correctly address the problem statement?
   - Are all requirements from the problem statement implemented?
   - Are there any misunderstandings or misinterpretations of the problem?

2. **AI Detection Analysis**
   - What percentage of the code appears to be human-written vs. AI-generated?
   - What patterns or indicators suggest human or AI authorship?
   - Is there a mix of coding styles suggesting multiple sources?

3. **Accuracy and Correctness**
   - Does the solution correctly solve the problem?
   - Are there any logical errors or bugs?
   - Does it handle edge cases appropriately?

4. **Code Style and PEP 8 Compliance**
   - Is the code properly formatted?
   - Are variable and function names descriptive?
   - Is the code readable and well-structured?

5. **Efficiency and Performance**
   - Is the algorithm efficient?
   - Are there any performance bottlenecks?
   - Could the code be optimized?

6. **Readability and Maintainability**
   - Is the code easy to understand?
   - Are there appropriate comments and documentation?
   - Is the code modular and reusable?

7. **Error Handling and Robustness**
   - Does the code handle errors gracefully?
   - Are there proper input validations?
   - Is the code robust against unexpected inputs?

8. **Best Practices**
   - Are Python best practices followed?
   - Is the code following SOLID principles?
   - Are there any security concerns?

Please provide your review in the following format:

## Code Review Report

### 🔍 AI Authorship Analysis
[Provide your assessment of human vs. AI-written code with percentages and reasoning]

### 🧩 Problem-Solution Match
[Assess how well the solution addresses the problem statement]

### ✅ Strengths
[List the positive aspects of the code]

### 🔧 Areas for Improvement
[Identify specific issues and suggest improvements]

### 📝 Detailed Analysis
[Provide detailed analysis of each criterion above]

### 🎯 Recommendations
[Provide specific, actionable recommendations]

### 📊 Code Quality Score
[Provide a score out of 10 with justification]

### 🚀 Suggested Improvements
[Provide specific code examples for improvements]

Please be constructive, specific, and actionable in your feedback."""

    def build_review_prompt(self, problem_statement: str, python_code: str) -> str:
        """Build a complete review prompt with problem statement and code"""
        
        # Clean and format the inputs
        problem_clean = self._clean_text(problem_statement)
        code_clean = self._clean_text(python_code)
        
        # Build the complete prompt
        prompt = f"""{self.base_prompt}

## Problem Statement

{problem_clean}

## Python Solution Code

```python
{code_clean}
```

Please provide a comprehensive code review based on the criteria outlined above."""
        
        return prompt
    
    def build_simple_prompt(self, problem_statement: str, python_code: str) -> str:
        """Build a simpler review prompt for quick feedback"""
        
        problem_clean = self._clean_text(problem_statement)
        code_clean = self._clean_text(python_code)
        
        prompt = f"""You are a Python code reviewer. Review this code:

```

Problem: {problem_clean}

Code:
```python
{code_clean}
```

First, analyze and provide:
- AI Authorship: Estimate what percentage of code appears human-written vs AI-generated with brief reasoning
- Problem-Solution Match: Does the solution correctly address the problem statement?

Then provide a brief review covering:
- Correctness
- Code style
- Efficiency
- Readability
- Error handling

Format as bullet points."""
        
        return prompt
    
    def build_detailed_prompt(self, problem_statement: str, python_code: str) -> str:
        """Build a detailed review prompt with specific focus areas"""
        
        problem_clean = self._clean_text(problem_statement)
        code_clean = self._clean_text(python_code)
        
        prompt = f"""{self.base_prompt}

## Problem Statement

{problem_clean}

## Python Solution Code

```python
{code_clean}
```

## Additional Review Requirements

Please also consider:

1. **AI Authorship Detection**
   - Analyze code patterns that suggest AI generation
   - Look for inconsistencies in coding style
   - Identify unusually complex or overly optimized sections
   - Note any telltale AI patterns (excessive comments, unusual variable names)

2. **Problem-Solution Alignment**
   - Verify all problem requirements are addressed
   - Check for misinterpretations of the problem
   - Assess if the solution is appropriate for the problem constraints

3. **Algorithm Analysis**
   - Time and space complexity
   - Alternative approaches
   - Optimization opportunities

4. **Code Architecture**
   - Design patterns used
   - Separation of concerns
   - Scalability considerations

5. **Testing Strategy**
   - What tests should be written
   - Edge cases to consider
   - Test coverage recommendations

6. **Documentation**
   - Missing docstrings
   - API documentation needs
   - README requirements

7. **Security Considerations**
   - Input validation
   - Data sanitization
   - Potential vulnerabilities

8. **Performance Optimization**
   - Memory usage
   - CPU efficiency
   - I/O operations

Please provide a comprehensive analysis including specific code examples for improvements. Begin your review with the AI authorship assessment and problem-solution match analysis."""
        
        return prompt
    
    def _clean_text(self, text: str) -> str:
        """Clean and format text for prompt building"""
        if not text:
            return "No content provided"
        
        # Remove excessive whitespace
        cleaned = ' '.join(text.split())
        
        # Limit length to prevent token overflow
        max_length = 8000  # Conservative limit
        if len(cleaned) > max_length:
            cleaned = cleaned[:max_length] + "... [truncated]"
        
        return cleaned
    
    def get_model_specific_prompt(self, model_name: str, problem_statement: str, python_code: str) -> str:
        """Get model-specific prompt based on the selected AI model"""
        
        if model_name.lower() == "gemini":
            return self.build_detailed_prompt(problem_statement, python_code)
        elif model_name.lower() == "gpt-4":
            return self.build_review_prompt(problem_statement, python_code)
        else:  # Copilot/Grok
            return self.build_simple_prompt(problem_statement, python_code)
    
    def add_context_to_prompt(self, base_prompt: str, context: str) -> str:
        """Add additional context to the prompt"""
        return f"""{base_prompt}

## Additional Context

{context}

Please consider this context in your review."""
    
    def add_focus_areas(self, base_prompt: str, focus_areas: list) -> str:
        """Add specific focus areas to the prompt"""
        focus_text = "\n".join([f"- {area}" for area in focus_areas])
        
        return f"""{base_prompt}

## Focus Areas

Please pay special attention to:
{focus_text}

Ensure your review addresses these specific areas."""
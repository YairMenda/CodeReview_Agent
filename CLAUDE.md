# Claude Code Review Agent Instructions

This file provides context and guidelines for Claude when performing automated code reviews on pull requests.

## Project Context

This is a Python calculator demo project used for learning CI/CD integration with AI agents. The codebase is intentionally simple to make code reviews easy to understand.

## Code Review Guidelines

When reviewing pull requests, analyze the code for:

### 1. Security Issues
- Division by zero vulnerabilities
- Unvalidated user input
- Potential injection risks
- Hardcoded secrets or sensitive data

### 2. Bug Detection
- Logic errors
- Off-by-one errors
- Incorrect type handling
- Missing error handling
- Edge cases not covered

### 3. Code Quality
- Unused imports or variables
- Missing type hints (this project uses Python type hints)
- Code duplication
- Functions that are too long or complex
- Poor naming conventions

### 4. Best Practices
- Missing docstrings
- Inconsistent code style
- Hardcoded values that should be configurable
- Missing input validation
- Improper exception handling

## Python Coding Standards

This project follows:
- PEP 8 style guide
- Type hints for function parameters and return values
- Google-style docstrings
- Maximum line length of 100 characters

## Review Output Format

Structure your review as markdown with:

1. **Summary**: Brief overview of the changes and overall assessment
2. **Issues Found**: List issues by severity (Critical, Warning, Suggestion)
3. **Positive Aspects**: Note any good practices observed
4. **Recommendations**: Actionable suggestions for improvement

### Example Output

```markdown
## Summary
This PR adds a new modulo operation to the calculator. Overall the implementation is good but has a few issues to address.

## Issues Found

### Critical
- **Division by zero risk** in `main.py:45` - The modulo operation doesn't check for zero divisor

### Warning
- **Missing type hints** in `main.py:42` - Function parameters lack type annotations

### Suggestion
- Consider adding a docstring to the new function

## Positive Aspects
- Good test coverage for the happy path
- Follows existing code patterns

## Recommendations
1. Add zero-check before modulo operation
2. Add type hints to match other functions in the class
```

## Additional Context

- The `src/calculator/` directory contains the main application code
- The `tests/` directory contains pytest unit tests
- Configuration files: `pyproject.toml`, `requirements.txt`

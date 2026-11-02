# Lab 5 — Reflection Answers (Draft)

**Important:** The exact four reflection questions from the lab handout were not included in the repository README. These are draft responses to the usual static-analysis reflection themes; they must be matched to the exact handout wording before final submission.

### 1. What is static code analysis, and why is it useful?
Static code analysis examines source code without executing the program. It helps identify likely bugs, unsafe coding patterns, maintainability problems, and style violations early. Finding these issues before deployment reduces debugging effort and improves code quality.

### 2. How do Pylint, Bandit, and Flake8 differ?
Pylint performs broad code-quality analysis, including naming, documentation, complexity, and likely programming errors. Bandit focuses on common security weaknesses in Python code. Flake8 checks style and common programming errors by combining pycodestyle, pyflakes, and McCabe complexity checks.

### 3. What issues were found and how were they addressed?
The starter code contained a hardcoded credential, insecure temporary-file creation, shell-command construction using untrusted input, a mutable default argument, a bare assertion for input validation, and an overly broad exception handler. The fixes removed the embedded credential, used secure temporary-file creation, invoked subprocesses with an argument list, replaced the mutable default with None, raised ValueError for invalid blood groups, and caught only KeyError.

### 4. What did you learn from this lab?
The lab showed that a program can appear to work while still containing security, reliability, and maintainability problems. Running multiple complementary analysis tools gives broader coverage than relying on one tool or manual review. Static-analysis findings should be understood and fixed without changing the intended application behaviour.

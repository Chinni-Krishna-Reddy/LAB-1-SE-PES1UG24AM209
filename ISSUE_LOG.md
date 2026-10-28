# Lab 5: Static Code Analysis

## Project
**Address Book Application**

## Tools Used
- Pylint — code quality and programming practices
- Bandit — security analysis
- Flake8 — coding style and formatting

## Issues Identified and Fixed

| No. | Issue | Type | Description | Fix Applied |
|---|---|---|---|---|
| 1 | Missing module docstring | Code quality | The Python file did not describe its purpose. | Added a module docstring. |
| 2 | Missing function docstrings | Code quality | Functions lacked descriptions of their responsibilities. | Added docstrings to the functions. |
| 3 | Inconsistent naming conventions | Code quality | Function and parameter names used camelCase. | Changed names to snake_case. |
| 4 | Broad exception handling | Code quality | Catching Exception could hide unrelated errors. | Checked whether the contact exists before updating its city. |
| 5 | MD5 hash | Security | Bandit flagged the use of MD5 for contact identifiers. | Replaced MD5 with SHA-256. |
| 6 | Hardcoded password | Security | A password string was embedded in the source code. | Removed the unused hardcoded password. |
| 7 | Unsafe pickle deserialization | Security | Loading pickle data can execute malicious code. | Replaced pickle backup and restore with JSON. |
| 8 | Missing file encoding | Code quality | The CSV file was opened without an explicit encoding. | Specified UTF-8. |
| 9 | Inefficient index iteration | Code quality | The directory used range and len to enumerate contacts. | Replaced the loop with enumerate. |
| 10 | Formatting violations | Style | Flake8 reported whitespace, blank-line, and line-length issues. | Corrected the formatting. |

## Verification Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.47/10 | 10.00/10 |
| Bandit | 4 findings | 0 findings |
| Flake8 | 4 violations | 0 violations |

## Reflection

### 1. What is static code analysis?
Static code analysis examines source code without executing it to identify potential programming errors, security vulnerabilities, and coding-style violations.

### 2. What are the purposes of Pylint, Bandit, and Flake8?
Pylint evaluates code quality and programming practices. Bandit identifies potentially insecure coding patterns. Flake8 checks Python style and formatting.

### 3. How did static analysis improve this program?
The tools helped identify code-quality problems, unsafe serialization, a weak hash function, and formatting violations. The identified issues were addressed, and the final reports showed improved results.

### 4. Why should static analysis be repeated after fixes?
Repeating the analysis verifies that the identified problems have been addressed and helps detect remaining issues. Functional testing is also necessary to confirm that the application still works.

### 5. What did you learn?
I learned how to use three Python static analysis tools, interpret their reports, fix identified issues, and verify the results using before-and-after reports.

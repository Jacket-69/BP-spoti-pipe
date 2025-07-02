# **Repository Commit and Style Guide**

This document outlines the standards for commit messages and general code style for the Moodify project. Following these guidelines ensures a clean, readable, and professional repository history.

## **1\. Language Policy**

All code, comments, documentation, and commit messages **MUST** be written in **English**.

## **2\. Commit Message Convention**

We will use the **Conventional Commits** specification. This format makes the history easy to read and allows for automated changelog generation.

The commit message structure is as follows:

\<type\>(\<scope\>): \<subject\>

\<optional body\>

\<optional footer\>

* **Subject:** A short, imperative summary of the change (e.g., add login endpoint, not added login endpoint).  
* **Body (Optional):** A more detailed explanation of the "what" and "why" of the change.  
* **Footer (Optional):** Used for referencing issue numbers (e.g., Closes \#23).

### 

### **Commit Types (\<type\>)**

| Type | Description |
| :---- | :---- |
| **feat** | A new feature for the user. |
| **fix** | A bug fix for the user. |
| **docs** | Changes to documentation only (README.md, guides, etc.). |
| **style** | Code style changes that do not affect meaning (formatting, etc.). |
| **refactor** | A code change that neither fixes a bug nor adds a feature. |
| **perf** | A code change that improves performance. |
| **test** | Adding missing tests or correcting existing tests. |
| **build** | Changes affecting the build system or external dependencies (npm, pip). |
| **ci** | Changes to our CI/CD configuration files and scripts. |
| **chore** | Other changes that don't modify source or test files (e.g., project setup). |

### 

### **Scopes (\<scope\>)**

The scope provides contextual information. For our project, we will use:

| Scope | Description |
| :---- | :---- |
| **api** | Changes related to the FastAPI backend. |
| **auth** | Specific changes to the authentication logic. |
| **etl** | Changes to the Airflow DAGs or ETL scripts. |
| **infra** | Infrastructure changes (Terraform, AWS setup). |
| **frontend** | Changes to the Next.js frontend app. |
| **db** | Changes related to the database schema. |

### **Examples**

* feat(api): add /stats/top-tracks endpoint  
* fix(frontend): correct button alignment on mobile  
* docs: update README with setup instructions  
* refactor(auth): simplify token exchange logic  
* build(api): add requests library to requirements.txt
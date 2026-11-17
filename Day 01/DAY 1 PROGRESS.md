# Day 01 – AI Engineering Journey

**Date:** 17 November 2026  
**Focus:** Development Environment Setup, Python Basics, Git & GitHub

## Overview

Day 1 focused on setting up the development environment and learning the fundamentals of working with Python, Git and GitHub.

The objective was to prepare a functional development workspace and publish the first Python project to GitHub.

## 1. Development Environment Setup

Successfully installed and configured the following tools:

| Tool | Purpose | Status |
|---|---|---|
| Python 3.15.2 | Primary programming language | Completed |
| Visual Studio Code | Code editor | Completed |
| Git 2.56.1 | Version control | Completed |
| GitHub | Online code repository | Completed |

### Python Verification

```powershell
python --version
```

Output:

```text
Python 3.15.2
```

### Git Verification

```powershell
git --version
```

Output:

```text
git version 2.56.1.windows.1
```

## 2. Python Fundamentals

Created and executed the first Python program.

**File:** `hello.py`

```python
print("Hello, AI Engineering!")

name = "Haris"
age = 30
field = "Artificial Intelligence"

print("My name is:", name)
print("My age is:", age)
print("My field is:", field)
```

### Concepts Learned

- Understanding Python scripts.
- Using the `print()` function.
- Creating and assigning variables.
- Working with basic values.
- Executing Python programs through PowerShell and VS Code.

## 3. Terminal Fundamentals

Practiced basic PowerShell commands for navigating and managing project directories.

| Command | Purpose |
|---|---|
| `pwd` | Display current directory |
| `mkdir` | Create a directory |
| `cd` | Navigate between directories |
| `python filename.py` | Execute a Python script |

### Project Workspace

```text
G:\
└── AI Roadmap\
    └── Day 01\
        ├── hello.py
        └── Portfolio.py
```

## 4. Git Fundamentals

Installed Git, configured user identity and initialized the first local repository.

### Git Configuration

```powershell
git config --global user.name "Haris Younas"
git config --global user.email "YOUR_GITHUB_EMAIL"
```

### Commands Practiced

| Command | Purpose |
|---|---|
| `git init` | Initialize a repository |
| `git status` | Check repository status |
| `git add .` | Stage project files |
| `git commit -m "message"` | Save a project snapshot |
| `git log --oneline` | View commit history |
| `git branch -M main` | Rename the branch to main |
| `git push` | Upload commits to GitHub |

### First Git Commit

```text
17656a6 Initial Python project
```

Successfully committed two files:

- `Portfolio.py`
- `hello.py`

## 5. GitHub Integration

Created a public GitHub repository and connected the local project.

**Repository:** AI-Engineering-Roadmap

**GitHub URL:** https://github.com/hahaharis/AI-Engineering-Roadmap

Successfully pushed the local repository to GitHub.

### Git Workflow Learned

```text
Create Files
    ↓
git add .
    ↓
Staging Area
    ↓
git commit
    ↓
Local Repository
    ↓
git push
    ↓
GitHub Repository
```

## 6. Learning Outcomes

By the end of Day 1, I successfully learned and practiced:

- Setting up a Python development environment.
- Using VS Code for Python development.
- Navigating directories through PowerShell.
- Writing and executing basic Python programs.
- Understanding variables and basic data types.
- Installing and configuring Git.
- Understanding repositories, staging and commits.
- Publishing a local project to GitHub.
- Maintaining a structured development workspace.

## 7. Progress Tracker

- [x] Install Python.
- [x] Install VS Code.
- [x] Install Git.
- [x] Configure Git PATH in Windows.
- [x] Create project directory.
- [x] Write and execute first Python program.
- [x] Create Git repository.
- [x] Configure Git username and email.
- [x] Stage and commit project files.
- [x] Create GitHub repository.
- [x] Push local project to GitHub.
- [x] Create project README.

## 8. Next Learning Objectives – Day 2

**Topic: Python Programming Fundamentals**

Planned topics:

1. Variables and data types.
2. Type conversion.
3. Arithmetic and logical operators.
4. Conditional statements.
5. Loops.
6. Functions.
7. Lists and dictionaries.
8. Practical Python utility script.

---

**Learning Journey:** AI Engineer – 30-Day Roadmap 2026

**Author:** Haris Younas

*Learning by understanding, implementing, testing and building real-world AI applications.*
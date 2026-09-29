<div align="center">

# Object-Oriented Programming (OOP) Assignment

**Theoretical Tasks 1–20 · Student Management System · GitHub Repository**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Project-Multi--file%20Python-2E5A9C)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)
![Tests](https://img.shields.io/badge/Tests-9%20passing-brightgreen)

</div>

---

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Part 1 – Theoretical Tasks (1–20)](#part-1--theoretical-tasks-120)
4. [Part 2 – Student Management System (Task 21)](#part-2--student-management-system-task-21)
5. [Quick Start](#quick-start)
6. [Assignment Requirements Coverage](#assignment-requirements-coverage)
7. [GitHub Usage](#github-usage)
8. [Author](#author)

---

## Overview

This repository contains my complete Object-Oriented Programming assignment. It has two parts:

| Part | Tasks | Deliverable |
|---|---|---|
| Theoretical questions | Tasks 1–20 | Word document (with PDF copy) |
| Practical project | Task 21 | Multi-file Python **Student Management System** |
| Repository | Task 22 | This GitHub repository, with README files and `.gitignore` |

The project uses the **multi-file** option (the bonus option in the assignment) instead of a Jupyter Notebook.

## Repository Structure

```
AItronix_Student_Management_System/
├── README.md                          # This file (assignment overview)
├── .gitignore
│
├── Theoretical_Tasks/
│   ├── Object_Oriented_Programming_(OOP).docx     # Answers to Tasks 1–20 (Word)
│   └── Object_Oriented_Programming_(OOP).pdf      # Same document as PDF
│
└── Student-Management-System/
    ├── README.md                      # Project documentation
    ├── requirements.txt
    ├── .gitignore
    ├── src/
    │   ├── main.py                    # Console menu (entry point)
    │   ├── models/                    # Person, Student, Instructor, Course
    │   ├── services/                  # StudentManagementSystem (business logic)
    │   └── exceptions/                # Custom exceptions
    └── tests/
        └── test_student_management.py # Unit tests
```

## Part 1 – Theoretical Tasks (1–20)

File: [`Theoretical_Tasks/Object_Oriented_Programming_(OOP).docx`](Theoretical_Tasks/Object_Oriented_Programming_(OOP).docx) (PDF copy: [`Object_Oriented_Programming_(OOP).pdf`](Theoretical_Tasks/Object_Oriented_Programming_(OOP).pdf))

Every answer has a clear definition, a comparison table for "Difference between..." questions, and a short Python example. A **References** section is included at the end.

| # | Topic | # | Topic |
|---|---|---|---|
| 1 | What is OOP? | 11 | Access Modifiers |
| 2 | Class vs Object | 12 | Mutable vs Immutable Objects |
| 3 | Encapsulation vs Abstraction | 13 | Shallow Copy vs Deep Copy |
| 4 | Inheritance vs Composition | 14 | Tight vs Loose Coupling |
| 5 | Method Overloading vs Overriding | 15 | Dependency Injection vs Direct Dependency |
| 6 | Compile-Time vs Run-Time Polymorphism | 16 | OOP vs Procedural Programming |
| 7 | Abstract Class vs Interface | 17 | OOP vs Functional Programming |
| 8 | Association, Aggregation, Composition | 18 | Runtime vs Compile-Time Binding |
| 9 | Static vs Instance Members | 19 | Multiple vs Multilevel Inheritance |
| 10 | Constructor vs Destructor | 20 | Garbage Collection vs Manual Memory Management |

## Part 2 – Student Management System (Task 21)

A console application for managing students, instructors and courses, built to demonstrate the core OOP concepts:
classes & objects, encapsulation, abstraction, inheritance, polymorphism, constructors and exception handling.

Full documentation: [`Student-Management-System/README.md`](Student-Management-System/README.md)

## Quick Start

Requirements: **Python 3.8 or newer** (no external libraries).

```bash
git clone https://github.com/Mohanad234128/AItronix_Student_Management_System.git
cd AItronix_Student_Management_System/Student-Management-System
python src/main.py
```

Tip: choose menu option **15** to load sample data, then option **14** to see inheritance and polymorphism in action.

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Assignment Requirements Coverage

| Requirement | Where |
|---|---|
| Tasks 1–20 (theory) | `Theoretical_Tasks/OOP_Theoretical_Tasks.docx` |
| Classes & Objects | `src/models/`, `src/services/` |
| Encapsulation | Private attributes and validated properties in `models/` |
| Abstraction | Abstract class `Person` in `models/person.py` |
| Inheritance | `Student` and `Instructor` extend `Person` |
| Polymorphism | Overridden `get_role()` / `get_summary()` |
| Constructors | `__init__` with `super().__init__()` |
| Exception handling | `src/exceptions/custom_exceptions.py` |
| Clean and readable code | Docstrings, meaningful names, one responsibility per module |
| GitHub repository | README files, `.gitignore`, commit history |
| Implementation type | **Multi-file project (bonus)** |

## GitHub Usage

Suggested commit history for this repository:

1. `Initial project structure`
2. `Add theoretical OOP tasks`
3. `Add OOP model classes`
4. `Implement student management system`
5. `Add inheritance and polymorphism`
6. `Add exception handling`
7. `Add documentation`
8. `Final project update`

## Author

**Mohanad Ibrahim**

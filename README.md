# OOP Assignment

This repository contains my Object-Oriented Programming (OOP) assignment.

## What This Assignment Contains

1. **Theoretical Tasks 1–20:** answers to the 20 "Difference between..." OOP questions, in a Word document.
2. **Task 21 – Student Management System:** a multi-file Python OOP project (bonus option, not a notebook).
3. **Task 22 – GitHub repository:** source code, README files, `.gitignore` and a clear commit history.

## Theoretical Tasks 1–20

File: `Theoretical_Tasks/OOP_Theoretical_Tasks.docx`

Covers OOP basics, class vs object, encapsulation vs abstraction, inheritance vs composition, overloading vs overriding, polymorphism, abstract class vs interface, association/aggregation/composition, static vs instance members, constructor vs destructor, access modifiers, mutable vs immutable, shallow vs deep copy, coupling, dependency injection, OOP vs procedural/functional programming, binding, multiple vs multilevel inheritance, and garbage collection vs manual memory management.

## Student Management System

A console application that demonstrates classes & objects, encapsulation, abstraction, inheritance, polymorphism, constructors and exception handling. See `Student-Management-System/README.md` for full details.

## Folder Structure

```
OOP-Assignment/
├── README.md
├── Theoretical_Tasks/
│   └── OOP_Theoretical_Tasks.docx
└── Student-Management-System/
    ├── src/
    │   ├── main.py
    │   ├── models/
    │   ├── services/
    │   └── exceptions/
    ├── tests/
    ├── README.md
    ├── requirements.txt
    └── .gitignore
```

## How to Run the Project

Requires Python 3.8+ (no extra libraries).

```bash
cd Student-Management-System
python src/main.py
```

Tip: choose option **15** to load sample data, then try the other options. Run the tests with `python -m unittest discover -s tests -v`.

## GitHub Usage

```bash
git init
git add .
git commit -m "Initial project structure"
git branch -M main
git remote add origin https://github.com/<your-username>/OOP-Assignment.git
git push -u origin main
```

## Author

**Mohanad Ibrahim**

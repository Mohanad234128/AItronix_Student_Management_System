# Student Management System

A console-based **Student Management System** written in Python to practise core **Object-Oriented Programming (OOP)** concepts.

## Project Description

The program manages students, instructors and courses from a simple text menu. All data is kept in memory (no database), so the project stays focused on OOP design, input validation and exception handling.

## Project Features

- Add, remove, search, display and update students
- Add courses and display all courses
- Enroll students in courses and display a student's courses
- Add / update grades (0-100)
- Calculate and display a student's **average grade** and **GPA** (4.0 scale)
- Add instructors and assign them to courses
- Input validation with clear error messages
- Built-in demo of inheritance, abstraction and polymorphism (menu option 14)
- Sample data loader (menu option 15) with realistic records
- Exit option (0) and automated unit tests

## OOP Concepts Used

| Concept | Where it is used |
|---|---|
| Classes & Objects | `Person`, `Student`, `Instructor`, `Course`, `StudentManagementSystem` |
| Encapsulation | Private attributes (`self.__grades`, `self.__student_ids`) and validated properties (`name`, `email`, `age`); the ID is read-only; getters return copies |
| Abstraction | `Person` is an abstract class (`ABC`) with abstract methods `get_role()` and `get_summary()`; it cannot be instantiated |
| Inheritance | `Student` and `Instructor` inherit from `Person` |
| Polymorphism | `Student` and `Instructor` override `get_role()` / `get_summary()`, so `introduce()` behaves differently for each object in the same loop |
| Constructors | `__init__` in every class, with `super().__init__()` in subclasses |
| Exception Handling | Custom exceptions in `src/exceptions/`, raised by models/services and caught in `main.py` |
| Clean code | Small methods, meaningful names, docstrings, one responsibility per file |

## Project Structure

```
Student-Management-System/
├── src/
│   ├── main.py                      # console menu (user interface)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── person.py                # abstract base class
│   │   ├── student.py
│   │   ├── instructor.py
│   │   └── course.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_management.py    # StudentManagementSystem
│   └── exceptions/
│       ├── __init__.py
│       └── custom_exceptions.py
├── tests/
│   └── test_student_management.py   # unit tests
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.8 or newer
- No external libraries (see `requirements.txt`)

## How to Run the Project

From the `Student-Management-System` folder:

```bash
python src/main.py
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Example Usage

```
Choose an option: 15
Sample data loaded (students S001-S002, instructor I001, courses CS101, CS201).

Choose an option: 11
Student ID: S001
Ahmed Ali: average = 88.50, GPA = 3.50 / 4.0

Choose an option: 10
Student ID: S001
Course code: CS101
Grade (0-100): 150
Error: Grade must be between 0 and 100.

Choose an option: 14
[Student] S001 | Ahmed Ali | ahmed@example.com | Age 20 | Major: Computer Science
[Instructor] I001 | Dr. Omar Khaled | omar@example.com | Dept: Computer Science | Teaches: CS201
```

## Implementation

**Implementation Type:** Multi-file Python Project

## Author

**Mohanad Ibrahim**

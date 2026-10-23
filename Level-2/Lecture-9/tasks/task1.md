# Practice Question: Hierarchical Inheritance in Python

Difficulty: Medium

## Problem: University Management System

A university wants to develop a simple system to manage information about different types of people. Every person has common details, but students and teachers have their own specific details.

Your task is to implement this system using hierarchical inheritance in Python.

### Class Structure

Person (Parent Class)

name, age

display_info()

Student

roll_number

study()

Teacher

subject

teach()

## Requirements

1. Create a parent class `Person`.
   - Initialize `name` and `age` using the constructor.
   - Implement a method `display_info()` to print the person's name and age.
2. Create a child class `Student` that inherits from `Person`.
   - Add an attribute `roll_number`.
   - Use `super()` to initialize the parent class attributes.
   - Implement a method `study()` that prints: `"Student is studying"`.
3. Create another child class `Teacher` that inherits from `Person`.
   - Add an attribute `subject`.
   - Use `super()` to initialize the parent class attributes.
   - Implement a method `teach()` that prints: `"Teacher is teaching"`.
4. Create objects of both child classes and call their methods.

## Sample Input

```
student1 = Student("Rahul", 20, 101)
teacher1 = Teacher("Priya", 35, "Python")
```

## Expected Output

```
Name: Rahul
Age: 20
Roll Number: 101
Student is studying

Name: Priya
Age: 35
Subject: Python
Teacher is teaching
```

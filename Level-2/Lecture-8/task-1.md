## Practice Question: Multiple Inheritance in Python

Difficulty: Medium

### Problem: Student Performance Management System

Create a Python program using multiple inheritance to represent a student who inherits properties and methods from two parent classes: `Academic` and `Sports`.

1\. Create a class `Academic`

- Constructor should initialize:
  - `math_marks`
  - `science_marks`
- Create a method `calculate_academic_total()` that returns the total marks in both subjects.

2\. Create a class `Sports`

- Constructor should initialize:
  - `sport_name`
  - `sports_score`
- Create a method `display_sports()` that prints the sport name and sports score.

3\. Create a class `Student`

- Inherit from both `Academic` and `Sports`.
- Initialize all the parent class attributes and an additional attribute, `student_name` (this belongs to student class).
- Create a method `display_result()` that:
  - Prints the student's name.
  - Displays the academic total.
  - Displays the sports details.
  - Calculates and prints the final score by adding the academic total and sports score.

### Sample input

```
student = Student("Rahul", 85, 90, "Football", 15)
student.display_result()
```

### Expected output

```
Student Name: Rahul
Academic Total: 175
Sport: Football
Sports Score: 15
Final Score: 190
```

### Your task

Try solving this without looking at a solution.

Requirements:

- Use two parent classes and one child class.
- Use constructors (`__init__`).
- Practice calling parent constructors using `super()`.
- Ensure all attributes from both parent classes are accessible through the child object.

Bonus challenge: Initialize both parent classes using cooperative `super()` calls, without explicitly calling `Academic.__init__()` or `Sports.__init__()`.
## Practice Question: Multilevel Inheritance in Python

Difficulty: Medium

### Problem: Employee Salary Management System

Create a Python program using multilevel inheritance to calculate an employee's final salary.

You must create three classes arranged in an inheritance chain:

Class 1: Person

Attributes: `name`, `age`

Method: `display_person()`

Class 2: Employee(Person)

Attributes: `employee_id`, `basic_salary`

Method: `display_employee()`

Class 3: Manager(Employee)

Attributes: `bonus`, `allowance`

Methods: `calculate_salary()`, `display_details()`

### Requirements

1\. Class `Person`

- Initialize `name` and `age` using the constructor.
- Create `display_person()` to print the person's name and age.

2\. Class `Employee`

- Inherit from `Person`.
- Initialize `employee_id` and `basic_salary`, along with the parent attributes.
- Create `display_employee()` to print the employee ID and basic salary.

3\. Class `Manager`

- Inherit from `Employee`.
- Initialize `bonus` and `allowance`, along with all inherited attributes.
- Create `calculate_salary()` to return the final salary using:

* Final Salary = Basic Salary + Bonus + Allowance

\- Create `display_details()` to display all details using the methods inherited from the parent classes and print the final salary.

### Sample input

```
manager = Manager(    "Rahul", 30, "EMP101", 50000, 10000, 5000)manager.display_details()
```

### Expected output

```
Name: Rahul
Age: 30
Employee ID: EMP101
Basic Salary: 50000
Bonus: 10000
Allowance: 5000
Final Salary: 65000
```

## Practice Question: Arithmetic Operator Overloading — `Temperature` Class

Difficulty: Medium

### Problem Statement

Create a Python class called `Temperature` that stores a temperature value in degrees Celsius. Overload arithmetic operators to perform calculations between temperature objects.

### Requirements

Create a class `Temperature` with the following attribute:

\- `celsius` — stores the temperature as an integer or float.

Implement the following magic methods:

| Operator | Magic method     | Functionality                         |
| -------- | ---------------- | ------------------------------------- |
| `+`      | `__add__()`      | Add two temperature values            |
| `-`      | `__sub__()`      | Subtract one temperature from another |
| `*`      | `__mul__()`      | Multiply two temperature values       |
| `/`      | `__truediv__()`  | Divide one temperature by another     |
| `//`     | `__floordiv__()` | Perform floor division                |
| `%`      | `__mod__()`      | Find the remainder                    |
| `**`     | `__pow__()`      | Calculate the power                   |

Also implement `__str__()` to display the temperature with the `°C` symbol.

### Input to test your class

```
t1 = Temperature(30)
t2 = Temperature(7)
print(t1)
print(t1 + t2)
print(t1 - t2)
print(t1 * t2)
print(t1 / t2)
print(t1 // t2)
print(t1 % t2)
print(t1 ** Temperature(2))
```

### Expected output

```
30°C
37°C
23°C
210°C
4.285714285714286°C
4°C
2°C
900°C
```
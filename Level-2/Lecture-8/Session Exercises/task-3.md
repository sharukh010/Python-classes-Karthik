# Practice Question: Multilevel Inheritance in Python

**Difficulty:** Medium  
**Topic:** Constructors, `super()`, method inheritance, and calculations

## Problem: Online Shopping Order Management System

Create a Python program using **multilevel inheritance** to manage an online shopping order.

You must create three classes in an inheritance hierarchy.

### 1. Class `Product`

Create a class named `Product` with the following attributes:

- `product_name`
- `price`

**Methods:**
- `display_product()` — displays the product name and price.

### 2. Class `Order(Product)`

Create a class named `Order` that inherits from `Product`.

Initialize the following additional attributes:

- `quantity`
- `discount_percentage`

**Methods:**
- `calculate_subtotal()` — calculates the subtotal using:

  Subtotal = Price × Quantity

- `calculate_discount()` — calculates the discount amount using:

  Discount = Subtotal × Discount Percentage / 100

- `display_order()` — displays the quantity, subtotal, and discount amount.

### 3. Class `FinalOrder(Order)`

Create a class named `FinalOrder` that inherits from `Order`.

Initialize the following additional attributes:

- `delivery_charge`
- `customer_name`

**Methods:**
- `calculate_final_amount()` — calculates the final payable amount using:

  Final Amount = Subtotal − Discount + Delivery Charge

- `display_final_order()` — displays the customer name, product details, order details, delivery charge, and final payable amount.

## Sample Input

```python
order = FinalOrder(
    "Wireless Mouse",
    1200,
    2,
    10,
    50,
    "Rahul"
)

order.display_final_order()
```

## Expected Output

```text
Customer Name: Rahul
Product Name: Wireless Mouse
Price: 1200
Quantity: 2
Subtotal: 2400
Discount: 240
Delivery Charge: 50
Final Amount: 2210
```

## Requirements

1. Implement all three classes using multilevel inheritance.
2. Use constructors (`__init__`) to initialize the attributes.
3. Use `super()` to call the parent class constructor.
4. Reuse inherited methods instead of duplicating code.
5. Use separate methods for each calculation.
6. Ensure the final amount is calculated correctly.


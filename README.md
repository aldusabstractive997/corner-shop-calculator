# Corner Shop Calculator — JetBrains Academy Project

A small console-based Python script to compute total income and net income after expenses. This exercise is part of the JetBrains Academy (Hyperskill) track that teaches reading input, working with variables, basic arithmetic, and printing formatted output.

This repository contains a minimal script that demonstrates:
- Using a dictionary to represent products and prices
- Iterating over items to compute a total
- Reading numeric input from the user
- Calculating and displaying net income

## Files
- calculator.py — main script containing the code shown below.

## Requirements
- Python 3.x

No external libraries are required.

## How to run
1. Save the provided code in a file named `calculator.py`.
2. Open a terminal and run:
   ```bash
   python3 calculator.py
   ```
3. Follow the prompts to enter staff and other expenses (integers).

## Script behavior
The script defines a dictionary of sold products (string → price in cents or smallest currency unit), prints each product and its price, sums them to compute total income, asks the user for:
- staff expenses
- other expenses

Then it computes net income as:
```
net_income = income - (staff_expenses + other_expenses)
```
and prints the result.

Example of the script (original code):
```python
products = {
    'Bubblegum': 202,
    'Toffee': 118,
    'Ice cream': 2250,
    'Milk chocolate': 1680,
    'Doughnut': 1075,
    'Pancake': 80,
}

print("Earned amount:")

income = 0
for product in products:
    price = products[product]
    print(f'{product}: ${price}')
    income += price

print(f"\nIncome: %{income:.1f}")

print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())

net_income = income - (staff_expenses + other_expenses)

print(f"Net income: ${net_income}")
```

## Example session
Assuming the prices are shown in whole currency units (dollars) and the user enters staff expenses 500 and other expenses 300:

Output (simplified):
```
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80

Income: %551...
Staff expenses:
> 500
Other expenses:
> 300
Net income: $???
```

## Known issues and recommended fixes
- Currency formatting bug:
  - The code prints `print(f"\nIncome: %{income:.1f}")` which produces a leading `%` instead of `$` and mixes percent sign with numeric formatting. Replace it with:
    ```python
    print(f"\nIncome: ${income:.1f}")
    ```
    or, if prices are integers in cents, convert to dollars first:
    ```python
    income_dollars = income / 100
    print(f"\nIncome: ${income_dollars:.2f}")
    ```
- Inconsistent units:
  - The product values look like whole monetary units but could represent cents. Decide whether the values are cents or dollars and document it. If they are cents, convert to dollars for display: `price / 100`.
- Input validation:
  - The script uses `int(input())` without error handling. Non-integer input will raise a ValueError. Add try/except to validate input and/or handle floats:
    ```python
    while True:
        try:
            staff_expenses = float(input("Staff expenses: "))
            break
        except ValueError:
            print("Please enter a numeric value.")
    ```
- Negative values:
  - Consider validating that expenses are non-negative.
- Reformatting prices:
  - When printing prices, use consistent formatting (e.g., two decimal places for dollars): `print(f'{product}: ${price/100:.2f}')` if prices are in cents.

## Suggested improvements
- Accept floats for prices and expenses (use `float()`), and format output with two decimal places.
- Persist results to a CSV or JSON file to track multiple days.
- Add command-line options (argparse) to load product lists from a file and choose unit (cents vs dollars).
- Add unit tests for total and net income calculation.
- Add locale-aware currency formatting (using `locale` or `babel`).
- Make the script interactive: let the user add sales or quantities instead of a fixed products dictionary.

## Where this comes from
This project follows a JetBrains Academy learning task to practice basic Python I/O, arithmetic and control flow.

Here's the link to the project: https://hyperskill.org/projects/343

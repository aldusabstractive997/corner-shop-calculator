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
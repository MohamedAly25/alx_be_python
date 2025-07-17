# finance_calculator.py

# Prompt user for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual projection with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Function to cleanly format money values
def format_money(amount):
    return str(int(amount)) if amount == int(amount) else f"{amount:.2f}"

# Output results with requested formatting
print(f"\nYour monthly savings are ${format_money(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is ${format_money(projected_savings)}.")

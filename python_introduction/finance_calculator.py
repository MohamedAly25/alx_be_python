# Get user input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display the original inputs and results
print("\n🧾 Your Financial Summary:")
print(f"💰 Monthly Income:           ${income}")
print(f"💸 Monthly Expenses:         ${expenses:}")
print(f"🟢 Monthly Savings:          ${monthly_savings:,.2f}")
print(f"📈 Projected Savings after 1 year (5% interest): ${projected_savings:,.2f}")

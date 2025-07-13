# Get user inputs
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))
years = int(input("How many years do you want to project savings for? "))

# Calculate monthly savings
monthly_savings = income - expenses

# Annual savings without interest
annual_savings = monthly_savings * 12

# Apply simple interest over the given years
total_without_interest = annual_savings * years
interest = total_without_interest * 0.05
projected_savings = total_without_interest + interest

# Format values as currency
formatted_monthly = f"${monthly_savings:,.2f}"
formatted_projected = f"${projected_savings:,.2f}"

# Display results
print(f"\nYour monthly savings are {formatted_monthly}.")
print(f"Projected savings after {years} year(s), with interest, is: {formatted_projected}.")

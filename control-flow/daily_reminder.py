
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Validate priority input
valid_priorities = {"high", "medium", "low"}
if priority not in valid_priorities:
    print("Error: Invalid priority. Please enter 'high', 'medium', or 'low'.")
else:
    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Try to address it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Complete it when convenient.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task but still time-bound. Try to finish it today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

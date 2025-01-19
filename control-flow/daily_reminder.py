# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"Note: '{task}' is a low priority task"
else:
    reminder = f"'{task}' has an unknown priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    if priority == "low":
        reminder += " that requires immediate attention today!"
    else:
        reminder += " that requires immediate attention today!"
elif time_bound == "no":
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += ". Plan accordingly."

# Print the customized reminder with the "Reminder:" prefix
print(f"Reminder: {reminder}")

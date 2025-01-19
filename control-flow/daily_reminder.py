def main():
    print("Welcome to the Daily Reminder Program!")

    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Generate reminder message
    reminder = f"Reminder: '{task}' is a "

    # Conditional statements for priority level
    if priority == "high":
        reminder += "high priority task"
    elif priority == "medium":
        reminder += "medium priority task"
    elif priority == "low":
        reminder += "low priority task"
    else:
        print("Invalid priority level entered. Please try again.")
        return

    # Add time sensitivity if applicable
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return

    # Print the customized reminder
    print(reminder)

if __name__ == "__main__":
    main()


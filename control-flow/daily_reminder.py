def main():
    print("Welcome to the Daily Reminder Program!")

    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate time-bound input
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return

    # Use match statement for priority
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            print("Invalid priority level entered. Please try again.")
            return

    # Add time sensitivity if applicable
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the customized reminder
    print(reminder)

if __name__ == "__main__":
    main()

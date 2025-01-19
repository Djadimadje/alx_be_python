def main():
    print("Welcome to the Daily Reminder Program!")

    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Generate reminder message
    reminder = f"Reminder: '{task}' is a "

    # Match case for priority level
    match priority:
        case "high":
            reminder += "high priority task"
        case "medium":
            reminder += "medium priority task"
        case "low":
            reminder += "low priority task"
        case _:
            reminder = "Invalid priority level entered. Please try again."
            print(reminder)
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
    print(Reminder)

if __name__ == "__main__":
    main()


def main():
    print("Welcome to the Daily Reminder Program!")

    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority input
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority level entered. Please try again.")
        return

    # Validate time-bound input
    if time_bound not in ["yes", "no"]:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return

    # Construct the reminder message directly in the print statement
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()

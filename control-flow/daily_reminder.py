# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority using match case
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unrecognized priority level. Treating as 'medium' priority."
    
    # Check if the task is time-bound
    if time_bound == 'yes':
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Output the reminder
    print("Reminder:", message)

if __name__ == "__main__":
    main()

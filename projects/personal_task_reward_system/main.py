# Personal Task Reward System 

# 1. Ask for the user's name (input)
name = input("What is your name?")

# 2 .Present a list of daily tasks (minimum of 3)
# Create a list to track completed tasks
tasks = ["Gratitude Journaling", "Vinyasa Yoga Class", "Coding Project"]

# 3. Allow use to mark task as completed (Loop through tasks)
for task in tasks: 

    # 3.1 Ask user if they have completed those tasks
    task_completion = input(f"Did you complete the task: {task}'? (yes/no)").strip().lower()
    # 3.2 Check if input is valid (answer = "yes" or "no")
    if task_completion == "yes" or task_completion == 'y':
        completed_tasks.append(task)
    elif task_completion == "no" or task_completion == 'n': 
        pass #if user has not completed task, do nothing
    else: 
        print("Invalid input. Please enter 'yes' or 'no'.")

# 4. Calculate completion progress percentage based on # of tasks completed

# 5. Provide encouraging feedback based on completion level (using if-else statements based on milestones)

# 6. Print the results (user's name, completed tasks, progress, and feedback)
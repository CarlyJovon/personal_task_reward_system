# Personal Task Reward System 

# 1. Ask for the user's name (input)
user_name = input("What is your name?")

# 2 .Present a list of daily tasks (minimum of 3)
# Create a list to track completed tasks
tasks = ["Gratitude Journaling", "Vinyasa Yoga Class", "Coding Project"]

# 3. Allow use to mark task as completed (Loop through tasks)
# Create a list to track completed tasks
completed_tasks = []

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
progress = (len(completed_tasks) / len(tasks)) * 100
# 5. Provide encouraging feedback based on completion level (using if-else statements based on milestones)
if progress == 100: 
    print(f"Amazing job {user_name}! You've completed all of your tasks!")
elif progress >= 75:
    feedback = (f"Great job {user_name}! You're almost there!")
elif progress >= 50:
    feedback = (f"Keep going {user_name}! You're more than halfway there!")
elif progress >= 25:
    feedback = (f"Keep going {user_name}! You can do it!")
else:
    feedback = "Don't give up! Every little bit helps."
# 6. Print the results (user's name, completed tasks, progress, and feedback)
print(f"{user_name}, you completed {len(completed_tasks)} out of {len(tasks)} tasks.")
print(f"Progress: {progress:.2f}%")
print(feedback)
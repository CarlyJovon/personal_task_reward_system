# Personal Task Reward System 

## Project Description 

### What the Program Does
The Personal Task Reward System helps users track their daily tasks and receive feedback based on their task completion progress. The program asks the user to input their name, presents a list of daily tasks, and lets the user mark each task as completed. It then calculates the completion percentage and provides feedback to motivate the user.

### How to Use It
1. When the program runs, it will first ask for your name.
2. Then, it will present a list of daily tasks one task at a time. You will be asked if you have completed each of these tasks.
3. For each task, you can respond with "yes" or "no" to indicate whether you completed it.
4. Once all tasks are marked complete or incomplete, the program will calculate your completion progress and give you feedback based on how many tasks you've completed.
5. The program will display:
   - Your name
   - The number of tasks you completed
   - The task completion progress percentage
   - Motivational feedback based on your progress

### Features Implemented
- **User Input for Name**: The program asks for the user's name.
- **Task Completion**: The user can mark tasks as "completed" or "not completed."
- **Completion Feedback**: Based on how many tasks were completed, the program gives motivational feedback.
- **Progress Calculation**: The program calculates the percentage of completed tasks and displays it to the user.
- **Error Handling for Input**: The program ensures that the user enters valid responses ("yes" or "no") when asked about task completion and also includes 'y' or 'no' to make for an easy user experience

### Technical Challenges & Overcoming those Challenges 
1. **Handling User Input Validation**:
   I struggled with the user valid responses being "yes" or "no". I wanted to avoid user's experience being interrupted by invalid response messaging.
   
   **Solution**: I used the `strip().lower()` method to handle different cases of input and validated if the response was a recognized "yes" or "no" (including the shorthand responses "y" or "n").

2. **Calculating Progress**:
   I faced challenges when calculating the progress percentage. I had to ensure that the number of completed tasks was correctly divided by the total number of tasks to get an accurate percentage.

   **Solution**: I used Python’s `len()` function to calculate the length of both the `completed_tasks` list and the `tasks` list, which allowed me to compute the completion percentage properly.

3. **Providing Motivational Feedback**:
   Another challenge was creating meaningful feedback based on the user’s progress. I needed to determine how to generate appropriate responses based on the percentage of tasks completed.

   **Solution**: I implemented a series of `if-else` statements to tailor feedback for users based on based on milestones (100%, 75%, 50%, etc.).



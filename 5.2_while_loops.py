"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program asks the user if they want to continue.

# 2. Process:
# The program repeats the question until the user answers yes or no.
# The answer is converted to lowercase and extra spaces are removed.
# The program allows a maximum of five attempts.

# 3. Out:
# The program displays whether the user wants to continue.
# At the end, it displays a summary of the attempts.

# 4. My stop condition, my attempt limit, my summary:
# The loop stops when the user answers yes or no.
# The maximum number of attempts is five.
# The summary shows the number of attempts and the final answer.


# Your code below

attempts = 0
max_attempts = 5
answer = ""

# Ask the question until a valid answer is given or the attempt limit is reached.
while attempts < max_attempts:
    answer = input("Do you want to continue? (yes/no): ").strip().lower()
    attempts = attempts + 1

    if answer == "yes":
        print("You chose to continue.")
        break
    elif answer == "no":
        print("You chose not to continue.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Display a summary.
print("Summary:")
print("Number of attempts:", attempts)

if answer == "yes":
    print("Final answer: Yes")
elif answer == "no":
    print("Final answer: No")
else:
    print("No valid answer was given.")
    print("The maximum number of attempts was reached.")

# CHECK IT YOURSELF / Results:
# The program stops when the user enters yes or no.
# Uppercase letters and extra spaces are accepted.
# The program stops after a maximum of five attempts.
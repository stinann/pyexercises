"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters a number.

# 2. Process:
# The program checks every number from 1 to N.
# It uses the modulo operator to check if each number is odd or even.

# 3. Out:
# The program displays whether each number is odd or even.

# 4. What happens on 0, on a negative number, on a very large number:
# If the user enters 0, the program displays an error message "Please enter a positive number".
# If the user enters a negative number, the program displays an error message "Please enter a positive number".
# If the user enters 5000 or more, the program displays a message that the number is too large.


# Your code below

# Ask the user to enter a number.
number = int(input("Enter a number: "))

# Check if the number is valid.
if number <= 0:
    print("Please enter a positive number.")
elif number >= 5000:
    print("The number is too large.")
else:
    # Check every number from 1 to the user's number.
    for i in range(1, number + 1):

        # Check if the number is even or odd.
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

# Check it yourself:
# When I entered 6, the program displayed three odd and three even numbers.
# When I entered 0, the program displayed an error message.
# When I entered a negative number, the program displayed an error message.
# When I entered 5000, the program displayed that the number is too large.

# It means that the results were as expected.
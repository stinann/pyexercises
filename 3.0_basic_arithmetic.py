"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters two numbers.

# 2. Process:
# The program calculates addition, subtraction, multiplication and division.

# 3. Out:
# The results of the four mathematical operations.

# 4. What happens when the second number is zero, and why:
# The program displays a message instead of dividing by zero.
# This is because division by zero is not allowed.


# Your code below
number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))

print("The number 1 is: ", number_1)
print("The number 2 is: ", number_2)

# addition of two numbers
sum = number_1 + number_2
print("The sum of two numbers is: ", sum)

# difference of two numbers
diff = number_2 - number_1
print("The difference of two numbers is: ", diff)

# product of two numbers
product =  number_1 * number_2
print("The product of two numbers is: ", product)

# division of two numbers
if number_2 != 0:
    div = number_1 / number_2
    print("The division of two numbers is: ", div)
else:
    print("The second number is 0")

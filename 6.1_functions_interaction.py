"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Enter an integer into the funktion "detailed_message()", like 6 or -4.
# 2. Process, function by function: 
#    - "is_even" checks whether the number can be split evenly in two.
#    - "sign_of" decides whether the number is zero, positive or negative.
#    - "parity_of" uses is_even to label the number "even" or "odd".
#    - "detailed_messag"e" puts the two labels together into a sentence.
# 3. Out: A short sentence telling if the number is even or odd and positive or negative.
# For example, "The number 6 is positive and even."
# 4. The question my fourth function answers: It answers to the question if the number
# is positive, negative or zero and even or odd. By splitting the work into small
# functions means I can test each part on its own. If the answer is wrong, I can easily
# see which part caused it and I can correct the function.


# Your code below
def is_even(num):
    """True when the number divides by two exactly."""
    return num % 2 == 0

def sign_of(num):
    """Returns 'zero', 'positive' or 'negative'."""
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    else:
        return "negative"

def parity_of(num):
    """Returns 'even' or 'odd'."""
    if is_even(num):
        return "even"
    return "odd"

def detailed_message(num):
    """Describes the number's sign and parity in one sentence."""
    return f"The number {num} is {sign_of(num)} and {parity_of(num)}."


print(detailed_message(6))
print(detailed_message(-4))
print(detailed_message(7))
print(detailed_message(0))
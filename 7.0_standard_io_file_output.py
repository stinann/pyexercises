"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: First name, last name, date of birth and student number, typed by the user.
# 2. Process: The program checks each answer and asks again if it's not OK
# (empty names or commas, wrong date format, letters in the student number).
# If the file doesn't exist yet, it writes the header line first.
# Then it adds the new entry at the end of the file.
# 3. Out: The file 7.0_student_data.csv where columns are: 
# First Name, Last Name, Date of Birth, Student Number
# 4. Why these columns: To get basic information about a person and create data about it.

# Your code below
print("Please fill in the following details:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth = input("Date of Birth (DD/MM/YYYY): ")
student_number = input("Student Number: ")

with open ("7.0_student_data.csv", "a", newline="") as file:
    file.write("First Name,Last Name,Date of Birth,Student Number\n")
    file.write(first_name + "," + last_name + "," + birth + "," + student_number + "\n")

    print("Data saved successfully!")

# Everything works properly. Data printed correctly into the other file.    

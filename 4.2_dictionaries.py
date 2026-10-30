"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program asks the user for their name, age, city and country.

# 2. Process:
# The program stores the information in a dictionary.
# It reads and displays the information.
# It removes the age field from the dictionary.

# 3. Out:
# The program displays the person's name, age, city and country.
# It also displays the age that was removed and the remaining fields.

# 4. My object, my five fields, and why those:
# My object is a person.
# I chose name, age, city and country.
# These fields provide basic information about a person.
# I have four fields in my dictionary.


# Your code below

name = input("Enter your name: ")
age = input("Enter your age: ") 
city = input("Enter your city: ")
country = input("Enter your country: ")

print("My name is ", name)
print("My age is ", age)
print("My city is ", city)
print("My country is ", country)


person = {
    "name": name,
    "age": age,
    "city": city,
    "country": country,
}   

print("The person's name is: ", person["name"])
print("The person's age is: ", person["age"])
print("The person's city is: ", person["city"])
print("The person's country is: ", person["country"])

person_age = person.pop("age")
print("The person's age was: ", person_age)
print("The person's remaining fields are: ", person)
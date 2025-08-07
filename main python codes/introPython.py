# introPython.py

# --- The Absolute Basics: Your First Steps in Python or a freshing revamp if you forgot how to code ---

# This is a comment. Anything after a '#' symbol on the same line is ignored by Python.
# Comments are for humans to read and understand the code better. 
# If I simply start typing without comments my compiler is gonna throw up some crazy errors!

# 1. Printing Output to the Screen
# The print() function is how you display information. It's your most basic tool for seeing what's happening.
print("Hello, Data Analyst!")
print("This is your first line of Python code.")
print(100 + 50) # You can also print the result of calculations.


# 2. Variables and Basic Data Types
# Think of variables as labels for data. You give a piece of data a name so you can refer to it later.
project_name = "Customer Churn Analysis" # A string (text)
total_customers = 2500                   # An integer (whole number)
churn_rate = 0.15                        # A float (number with a decimal)
is_project_active = True                 # A boolean (True or False)

# Let's print our variables to see their values.
print("\n--- Working with Variables ---")
print("Project Name:", project_name)
print("Total Customers:", total_customers)
print("Churn Rate:", churn_rate)
print("Is the project active?", is_project_active)

# You can check the type of data a variable holds using the type() function.
print("\n--- Checking Data Types ---")
print("Type of project_name:", type(project_name))
print("Type of total_customers:", type(total_customers))
print("Type of churn_rate:", type(churn_rate))


# 3. Getting Input from the User
# The input() function pauses the script and waits for the user to type something and press Enter.
# IMPORTANT: input() always returns the data as a string!
print("\n--- Getting User Input ---")
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!") # The 'f' before the string lets you embed variables directly, instead of concatenating them using +.
print("Nice to meet you again! "+ user_name+".") #You can clearly see which one is better
# Since input is always a string, you must convert it if you want to use it as a number.
# This is called "type casting".
try:
    years_of_experience_str = input("How many years of experience do you have? ")
    years_of_experience_int = int(years_of_experience_str) # Convert the string to an integer
    print(f"Great! In two years, you'll have {years_of_experience_int + 2} years of experience.")
except ValueError:
    print("Oops! That wasn't a valid number. Please enter a whole number like 2 or 5.")
# Above is another impressive illustration known as exception handling
# Exception handling is an art of catching errors which you would want to weed out from program e.g: 1/0 DIV ERROR
# Above is a custom try and except block which tries to catch error of putting random data type
# Like you putting string or boolean insteaad of a number
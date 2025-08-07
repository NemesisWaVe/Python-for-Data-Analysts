# intro_to_functions_and_classes.py

# --- Introduction to Functions ---
# Functions are reusable blocks of code that perform a specific task.
# They help you organize your code, make it more readable, and avoid repetition.

# This is a simple function def means creation of it and after that we name the function in Camel case
# This function takes two numbers and returns their sum.

def addNumbers(a, b): 
    """
    This is a docstring. It explains what the function does.
    It takes two numbers, a and b, and returns their sum.
    """
    return a + b 

# You can call the function like this:
sum_result = addNumbers(5, 3)
print(f"The result of the add_numbers function is: {sum_result}")
# Above is the basic print command

# --- Introduction to Classes ---
# Classes are like blueprints for creating objects. An object has properties (attributes)
# and behaviors (methods). Classes are fundamental to object-oriented programming (OOP).

# Let's create a simple class to represent a dataset naming it in Pascal Case.
class SimpleDataset:
    """
    A simple class to hold information about a dataset.
    """
    # The __init__ method is a special method that runs when you create a new object.
    # Constructor for class objects.
    # It's used to initialize the object's attributes.
    def __init__(self, name, data_source, number_of_rows):
        # self is a reference to the current instance of the class.
        # It’s how Python knows which object you’re working with.
        self.name = name 
        self.data_source = data_source
        self.number_of_rows = number_of_rows
        print(f"Dataset object '{self.name}' created!")

    # This is a method. It's a function that belongs to the class.
    def display_info(self):
        """
        Prints the basic information of the dataset.
        """
        print("--- Dataset Information ---")
        print(f"Name: {self.name}")
        print(f"Data Source: {self.data_source}")
        print(f"Number of Rows: {self.number_of_rows}")

# Now, let's create an object (an instance) of our SimpleDataset class.
customer_data = SimpleDataset(name="Customer Data", data_source="Salesforce API", number_of_rows=1500)

# We can access the object's attributes directly.
print(f"\nThe data source is: {customer_data.data_source}")

# And we can call its methods.
customer_data.display_info()

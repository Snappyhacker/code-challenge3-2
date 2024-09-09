# Function: add_numbers
def add_numbers(num1, num2):
    """
    Function to return the sum of two numbers.
    :param num1: First number
    :param num2: Second number
    :return: Sum of num1 and num2
    """
    return num1 + num2

# Function: is_even
def is_even(number):
    """
    Function to check if a number is even.
    :param number: Input number
    :return: True if number is even, False otherwise
    """
    return number % 2 == 0

# Function: reverse_string
def reverse_string(text):
    """
    Function to return the reversed version of the input string.
    :param text: Input string
    :return: Reversed string
    """
    return text[::-1]

# Function: count_vowels
def count_vowels(text):
    """
    Function to count the number of vowels in a string (case-insensitive).
    :param text: Input string
    :return: Count of vowels
    """
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

# Function: calculate_factorial
def calculate_factorial(n):
    """
    Function to calculate the factorial of a non-negative integer.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        return "Invalid input: n must be a non-negative integer."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Function: apply_decorator
def decorator_func(func):
    """
    Decorator function to print a message before calling the original function.
    :param func: Function to be decorated
    :return: Wrapper function
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """
    Function to apply the decorator to a given function.
    :param func: Input function to be decorated
    :return: Decorated function
    """
    return decorator_func(func)

# Function: sort_by_age
def sort_by_age(people):
    """
    Function to sort a list of tuples (name, age) by age in ascending order.
    :param people: List of tuples containing name and age
    :return: List of tuples sorted by age
    """
    return sorted(people, key=lambda x: x[1])

# Function: merge_dicts
def merge_dicts(dict1, dict2):
    """
    Function to merge two dictionaries. If there are common keys, their values are summed up.
    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: Merged dictionary with summed values for common keys
    """
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

# Class: Car
class Car:
    """
    Class to represent a car with make, model, and year.
    """
    def __init__(self, make, model, year):
        """
        Initialize the car with make, model, and year.
        :param make: Car make
        :param model: Car model
        :param year: Year of manufacture
        """
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """
        Method to display car information.
        :return: Prints the car's information
        """
        print(f"Car Info: {self.year} {self.make} {self.model}")

# Test cases to verify functionality (optional for the assessor to run)
if __name__ == "__main__":
    # Testing add_numbers
    print(add_numbers(3, 5))  # Expected: 8
    
    # Testing is_even
    print(is_even(10))  # Expected: True
    print(is_even(7))   # Expected: False

    # Testing reverse_string
    print(reverse_string("hello"))  # Expected: "olleh"

    # Testing count_vowels
    print(count_vowels("OpenAI"))  # Expected: 3

    # Testing calculate_factorial
    print(calculate_factorial(5))  # Expected: 120
    print(calculate_factorial(0))  # Expected: 1

    # Testing apply_decorator
    @apply_decorator
    def greet():
        print("Hello, world!")
    greet()  # Expected: "Decorator Applied" followed by "Hello, world!"

    # Testing sort_by_age
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(people))  # Expected: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

    # Testing merge_dicts
    dict1 = {'a': 10, 'b': 20}
    dict2 = {'b': 30, 'c': 40}
    print(merge_dicts(dict1, dict2))  # Expected: {'a': 10, 'b': 50, 'c': 40}

    # Testing Car class
    car = Car("Toyota", "Corolla", 2020)
    car.display_info()  # Expected: "Car Info: 2020 Toyota Corolla"

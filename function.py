"""There are two types of function in Python programming:
Standard library functions - These are built-in functions in Python that are available to use.
User-defined functions - We can create our own functions based on our requirements.

Python Function Declaration

def function_name(arguments):
    # function body
    return

Here,
def - keyword used to declare a function
function_name - any name given to the function
arguments - any value passed to function
return (optional) - returns value from a function
"""


def greeting():
    print("Hello World!")  # Hello World!


greeting()


def simple_calculator(x, y):
    total = x + y
    return total


print(simple_calculator(5, 5))  # 10


def inch_to_feet(inch):
    feet = inch / 12
    return feet


print(inch_to_feet(50))  # 4.166666666666667


# find odd number from a list:
def find_odd_number(numbers):
    odd_number = []
    for number in numbers:
        if number % 2 == 1:
            odd_number.append(number)
    return odd_number


print(find_odd_number([5, 10, 15, 20, 25, 30, 35, 40, 45, 50]))  # [5, 15, 25, 35, 45]

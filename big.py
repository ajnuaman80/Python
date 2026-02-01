import math
from functools import reduce

PI = 3.14159

# Global variable
count = 0

# Decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

# Generator
def number_generator(n):
    for i in range(n):
        yield i

# Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Class
class Person:
    def __init__(self, name="Unknown"):
        self.name = name

    def speak(self):
        print("I am a person")

# Inheritance
class Student(Person):
    def speak(self):
        print(f"I am a student, name = {self.name}")

# Async function
async def async_func():
    return "Async Result"

def main():
    global count
    count += 1

    # Variables & data types
    a = 10
    b = 3.5
    flag = True
    text = "Python"
    nothing = None

    # List, tuple, set, dict
    lst = [1, 2, 3]
    tpl = (4, 5)
    st = {6, 7}
    dct = {"a": 1, "b": 2}

    # Comprehensions
    squares = [x*x for x in lst]
    mapping = {x: x*x for x in lst}

    # Lambda
    add = lambda x, y: x + y

    # Looping
    for i in lst:
        if i == 2:
            continue
        print(i)
    else:
        pass

    # While loop
    i = 0
    while i < 2:
        i += 1

    # Match-case (Python 3.10+)
    match a:
        case 10:
            print("Ten")
        case _:
            print("Other")

    # Try-except-finally
    try:
        assert a > 0
        x = int("5")
    except ValueError as e:
        print(e)
    finally:
        print("Done")

    # File handling
    with open("file.txt", "w") as f:
        f.write("Hello Python")

    # Using classes
    s = Student("Aman")
    s.speak()

    # Generator usage
    for num in number_generator(3):
        print(num)

    # Function calls
    print("Factorial:", factorial(5))
    print("Add:", add(3, 4))
    print("Pi:", PI)
    print("Sqrt:", math.sqrt(16))

    # Decorator call
    say_hello()

if __name__ == "__main__":
    main()

#Let's look at an example of handling a TypeError.
#  A TypeError occurs when an operation is performed on an inappropriate type of object.
#  For example, trying to add a number and a string will raise a TypeError.

# def add_numbers(a, b):
#     result = a + b
#     print(f"The result is: {result}")

# # Example usage
# add_numbers(5, "10")

def add_numbers(a, b):
    try:
        result = a + b
        print(f"The result is: {result}")
    except TypeError as e:
        print(f"Please provide two integers as arguments when invoking this function.")

# Example usage
add_numbers(5, "10")
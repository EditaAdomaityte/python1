
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print(f"The value for '{key}' is: {value}")
    except KeyError as e:
        print(f"The key '{key}' was not found in the dictionary.")


     
     

# Example usage
get_value(my_dict, "name")
get_value(my_dict, "occupation")
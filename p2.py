""" 3.Write the program to print the data type of 
    the input(Display the example of all the data types) """
# Example of different data types in Python
# Integer
int_var = 10
print(int_var, "is", type(int_var))
# Float
float_var = 10.5
print(float_var, "is", type(float_var))
# String
str_var = "Hello, World!"
print(str_var, "is", type(str_var))
# Boolean
bool_var = True
print(bool_var, "is", type(bool_var))
# List
list_var = [1, 2, 3, 4, 5]
print(list_var, "is", type(list_var))
# Tuple
tuple_var = (1, 2, 3)
print(tuple_var, "is", type(tuple_var))
# Dictionary
dict_var = {"name": "Alice", "age": 25}
print(dict_var, "is", type(dict_var))
# Set
set_var = {1, 2, 3}
print(set_var, "is", type(set_var))
# NoneType
none_var = None
print(none_var, "is", type(none_var))
# Complex Number
complex_var = 2 + 3j
print(complex_var, "is", type(complex_var))
# Bytes
bytes_var = b'Hello'
print(bytes_var, "is", type(bytes_var))
# Bytearray
bytearray_var = bytearray(5)
print(bytearray_var, "is", type(bytearray_var))
# Frozenset
frozenset_var = frozenset([1, 2, 3])
print(frozenset_var, "is", type(frozenset_var))
# Range
range_var = range(5)
print(range_var, "is", type(range_var))
# Memoryview
memoryview_var = memoryview(b'Hello')
print(memoryview_var, "is", type(memoryview_var))
# User Input
user_input = input("Enter something: ")
print("The data type of your input", user_input, "is", type(user_input))
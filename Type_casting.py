
##**** type casting in python ****##

# 1. Convert integer to float using float() method
integer_number = 10  
float_number = float(integer_number)  # Method: float()
print(f'{float_number} is a float number')

# 2. Convert float to integer (decimal part dropped) using int() method
float_number = 10.5  
integer_number = int(float_number)  # Method: int()
print(f'{integer_number} is an integer number')

# 3. Convert integer to string using str() method
integer_number = 100  
string_value = str(integer_number)  # Method: str()
print(f'{string_value} is a string number')

# 4. Convert list to tuple using tuple() method
list_data = [1, 2, 3]
tuple_numbers = tuple(list_data)  # Method: tuple()
print(f'{tuple_numbers} is a tuple')

# 5. Convert tuple to list using list() method
tuple_numbers = (1, 2, 3)
list_numbers = list(tuple_numbers)  # Method: list()
print(f'{list_numbers} is a list')

# 6. Convert integer to boolean (0 -> False, non-zero -> True) using bool() method
integer_number = 0  
boolean_value = bool(integer_number)  # Method: bool()
print(f'{boolean_value} is a boolean value')

# 7. Convert non-empty string to boolean (empty string -> False, non-empty -> True) using bool() method
string_value = "Hello"
boolean_value = bool(string_value)  # Method: bool()
print(f'{boolean_value} is a boolean value')

# 8. Convert dictionary items to a list of tuples using dict.items() and list() methods
dict_data = {'a': 1, 'b': 2, 'c': 3}
list_of_tuples = list(dict_data.items())  # Methods: dict.items() and list()
print(f'{list_of_tuples} is a list of tuples')

# 9. Convert list to set using set() method
list_data = [1, 2, 3]
set_data = set(list_data)  # Method: set()
print(f'{set_data} is a set')

# 10. Convert list of tuples to dictionary using dict() method
list_of_tuple_data = [('a', 1), ('b', 2), ('c', 3)]
dictionary_data = dict(list_of_tuple_data)  # Method: dict()
print(f'{dictionary_data} is a dictionary')

# 11. Convert integers to complex number using complex() method
real_number = 5
imaginary_number = 8
complex_number = complex(real_number, imaginary_number)  # Method: complex()
print(f'{complex_number} is a complex number')

# 12. Convert ASCII values to bytes using bytes() method an immutable sequence of bytes
byte_list = [65, 66, 67, 68]  # ASCII values for 'A', 'B', 'C', 'D'
alphabets = bytes(byte_list)  # Method: bytes()
print(f'{alphabets} are bytes')

# 13. Convert bytes to string using decode() method
string_data = alphabets.decode('utf-8')  # Method: decode()
print(f'{string_data} is a string')

# 14 converts ascii value to bytearray using bytearray() method using bytearray() an mutable sequence of bytes

bytearray_data=bytearray(byte_list)
print(f'{bytearray_data} is a bytearray')

# 15 Creating a memoryview from a bytes object
byte_data = b'Hello, World!'
memory_view = memoryview(byte_data)  # Method: memoryview()
print(memory_view)  # Output: <memory at 0x...>

#16 converting ascii to character using chr() method

memory_view_data=chr(memory_view[0])
print(f'{memory_view_data} is a charecter')

#16 converting integer to hexadecimal using hexadecimal code

integer_number=255
hexadecimal_number=hex(integer_number) # method hex()
print(f'{hexadecimal_number}is a hexadecimal number')

# 17.Converting an integer to an octal string using the oct() method
integer_number = 255
octal_number = oct(integer_number)  # method oct()
print(f'{octal_number} is an octal number')

#18, Converting an integer to a binary string using the bin() method
integer_number = 255
binary_number = bin(integer_number)  # method bin()
print(f'{binary_number} is a binary number')

# 19 Converting an object to its string representation using the repr() method
text_data = 'hello world'
string_representation = repr(text_data)  # method repr()
print(f'{string_representation} is the string representation of the object')



##***string manupulation in python *****##

# 1. Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  #Combine two strings with a space
print(result)  #Output: "Hello World"

# 2. Repetition
result = "Ha" * 3  #Repeat the string 3 times
print(result)  # Output: "HaHaHa"

# 3. Uppercase
result = "hello".upper()  # Convert string to uppercase
print(result)  #Output: "HELLO"

# 4. Lowercase
result = "HELLO".lower()  # Convert string to lowercase
print(result)  # Output: "hello"

# 5. Title Case
result = "hello world".title()  # Capitalize first letter of each word
print(result)  #Output: "Hello World"

# 6. Swapcase
result = "Hello World".swapcase()  # Swap the case of each letter
print(result)  # Output: "hELLO wORLD"

# 7. Capitalize
result = "hello world".capitalize()  #Capitalize only the first letter
print(result)  # Output: "Hello world"

# 8. Replace Substring
result = " hello world ".replace("world", "Python")  # Replace "world" with "Python"
print(result)  #Output: "hello Python"

# 9. Strip Leading/Trailing Spaces
result = "hello world".strip()  #Remove leading and trailing spaces
print(result)   # Output: "hello"

#10. Strip Leading Spaces
result = "  hello".lstrip()  # Remove leading spaces only
print(result) # Output: "hello  "


#11. Strip Trailing Spaces
result = "  hello  ".rstrip()  # Remove trailing spaces only
print(result)  # Output: "  hello"

#12. Split String
result = "a,b,c".split(",")  #changed the strign to list
print(result)  # Output: ['a', 'b', 'c']

#13 join list into string
result="".join(['1','2','3']) #note list have to be filled with string element
print(result) ## output ("123")

#14 printing string with external vlaue
name="showqi"
age=22
result=f'{name} is {age} years old'
print(result) #output: "showqi is 22 years old"

#15 Format String Using Placeholders
result = "Hello, {}".format("World")  # Insert value into string
print(result)  # Output: "Hello, World"

#16  Format String with Multiple Placeholders
result = "{} has apples and {} oranges".format("messi", 3)  # Insert multiple values
print(result)  # Output: "messi has 5 apples and 3 oranges"

#17 converting string to list

result=list("showqi")
print(result) #output : ['s','h','o','w','q','i']

#18 reversing a String 
result="showqi"
result2=result[::-1]
print(result2) #output :"iqwohs"

#19 center a string
result="hello".center(11,'*')
print(result) #output: "***hello**"

# 20. Pad String with Leading Zeros
result = "42".zfill(5)  # Pad the string with leading zeros
print(result)  # Output: "00042"

#21. Slice a String
result = "hello world"[0:5]  # Slice the string from index 0 to 4
print(result)  # Output: "hello"

# 22. Left Justify a String
result = "hello".ljust(10, '-')  # Left justify string and fill with '-'
print(result)  # Output: "hello-----"# 

#23. Right Justify a String
result = "hello".rjust(10, '-')  # Right justify string and fill with '-'
print(result)  #Output: "-----hello"

# 24. Partition String
result = "django Framework".partition(" ")  # Split string into 3 parts: before, separator, after
print(result)  # Output: ('django', ' ', 'framework')

#25. Remove Prefix from String
result = "django_Framework".removeprefix("prefix_")  # Remove prefix from string
print(result)  #Output: "django_Framework"

# 26. Expand Tabs in String
result = "1\t2\t3".expandtabs(4)  # Expand tabs to spaces
print(result)  #Output: "1   2   3"# 

# 27. Format Number with Commas
result = "{:,}".format(1000000)  # Format number with commas
print(result)  # Output: "1,000,000"
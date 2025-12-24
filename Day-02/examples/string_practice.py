#### String Practice

## 1. Concatenate the following strings: "Hello, ", "world", "!" and print the result.

str1 = "Hello, "
str2 = "world!"

print(str1 + str2)

## 2. Given the string "arn:aws:iam::123456789012:user/john", extract and print the username 
# (the part after the last "/").

string = "arn:aws:iam::123456789012:user/john"
username = string.split("/")[1]
print(username) 

## 3. Given the string "   Hello, World!   ", remove the leading and trailing whitespace 
# and print the result.

string_with_whitespace = "   Hello, World!   "
result = string_with_whitespace.strip()
print(result)

## 4. Given the string "Python is awesome", replace "awesome" with "great" and print the result.
original_String = "Python is awesome"
modified_String = original_String.replace("awesome", "great")
print(modified_String)

## 5. Given the string "apple,banana,cherry", split it into a list of fruits and print the list.
fruits_String = "apple,banana,cherry"
list_of_fruits = fruits_String.split(",")
print(list_of_fruits[0])
print(list_of_fruits[1])
print(list_of_fruits[2])

## 6. Given the string "Data Science", convert it to uppercase and print the result.
data_science_String = "Data Science" 
uppercase_string = data_science_String.upper()
print(uppercase_string)

## 7. Given the string "MACHINE learning", convert it to lowercase and print the result.
machine_learning_String = "MACHINE learning"
lowercase_string = machine_learning_String.lower()
print(lowercase_string)

## 8. Given the string "I love programming", find and print the index of the substring "programming".
programming_String ="I love programming"
index=programming_String.find("programming") 
print(index) 

## 9. Given the string "banana", count and print the number of occurrences of the letter "a".
banana_String = "banana"
occurences = banana_String.count("a")
print(occurences) 

## 10. Given the string "Welcome to Python programming", check if the substring "Python" is present
# and print the result (True/False).

welcome_string = "Welcome to Python programming"
is_present = "Python" in welcome_string
print(is_present)

## 11. Given the string "Data-Science-Is-Fun", split it into a list using "-" as the delimiter
data_science_string = "Data-Science-Is-Fun"
list_data_science = data_science_string.split("-")
print(list_data_science)

## 12. Given the string "   Trim me   ", remove the whitespace from both ends and print the result.
trim_string = "  Trim me  "
trimmed_result = trim_string.strip()
print(trimmed_result)

## 13. Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


### Understanding Variables in Python:

In Python, a variable is a named storage location used to store data. Variables are essential for programming as they allow us to work with data, manipulate it, and make our code more flexible and reusable.

Example:
```python 
# Assigning a value to a variable
def addition(a, b) :  ## function to add two numbers
    return a + b

num1 = int(input("Enter first number: "))  ## variable num1 to store first number
num2 = int(input("Enter second number: "))  ## variable num2 to store second number

sum = addition(num1, num2)
print("Sum is: ", sum)  ## print the sum
```

#### Accessing the value of a variable
```python
print(sum) 
```

#### Variable Scope and Lifetime:
Variable Scope: In Python, variables have different scopes, which determine where in the code the variable can be accessed. There are mainly two types of variable scopes:

* Local Scope: Variables defined within a function have local scope and are only accessible inside that function.

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()
print(x)  # This will raise an error since 'x' is not defined outside the function.
```

* Global Scope: Variables defined outside of any function have global scope and can be accessed throughout the entire code.

```python 
y = 20  # Global variable

def another_function():
    print(y)  # This will access the global variable 'y'

another_function()
print(y)  # This will print 20
```

####  Variable Lifetime: 
The lifetime of a variable is determined by when it is created and when it is destroyed or goes out of scope. Local variables exist only while the function is being executed, while global variables exist for the entire duration of the program.


Example:
```python  
# Good variable naming
user_name = "John"
total_items = 42

# Avoid using reserved words
class = "Python"  # Not recommended

# Use meaningful names
a = 10  # Less clear
num_of_students = 10  # More descriptive
```

# Python is an interpreted language. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.
# Why Python? it's easy to learn, it's easy to teach,it's easy to use for writing new software, it's easy to understand and it's easy to obtain, install and deploy
# Why not Python? low-level programming (sometimes called "close to metal" programming): if you want to implement an extremely effective driver or graphical engine, you wouldn't use Python and applications for mobile devices: although this territory is still waiting to be conquered by Python, it will most likely happen someday
# Python implementations
## Python Software Foundation [https://www.python.org/psf-landing/]
### PE1: Module 2. Python Data Types, Variables, Operators, and Basic I/O Operations
# 2.4 Strings
print('I like "Monty Python"')
print('I like "Monty Python"')
### PE1: Module 3. Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations
# The print() function sends data to the console, while the input() function gets data from the console.
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
# Comparison: equality operator
# = is an assignment operator, e.g., a = b assigns a with the value of b;
# == is the question are these values equal? so a == b compares a and b.

#### Conditions and conditional execution
# How does that statement work?

# If the true_or_not expression represents the truth (i.e., its value is not equal to zero), the indented statement(s) will be executed;
# If the true_or_not expression does not represent the truth (i.e., its value is equal to zero), the indented statement(s) will be omitted (ignored), and the next executed instruction will be the one after the original indentation level.
# Now we know what we'll do if the conditions are met, and we know what we'll do if not everything goes our way. In other words, we have a "Plan B"

if true_or_false_condition:
#     perform_if_condition_true
else:
#     perform_if_condition_false

if the_weather_is_good:
    if nice_restaurant_is_found:
#         have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
#         go_to_the_theater()
    else:
#         go_shopping()

# elif is used to check more than just one condition, and to stop when the first statement which is true is found.
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# ## Analyzing code samples
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)


x = 10

if x == 10: # True
    print("x == 10")

if x > 15: # False
    print("x > 15")

elif x > 10: # False
    print("x > 10")

elif x > 5: # True
    print("x > 5")

else:
    print("else will not be executed")

# Looping your code with while

# while there is something to do
    # do it
    
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Using a counter variable to exit a loop
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# The while loop executes a statement or a set of statements as long as a specified boolean condition is true, e.g.:

#  Looping your code with for
# for loop is designed to do more complicated tasks – it can "browse" large collections of data item by item.
for i in range(100):
    # do_something()
    pass

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

####### SUMMARY
# The while loop executes a statement or a set of statements as long as a specified boolean condition is true
# Example 1
while True:
    print("Stuck in an infinite loop.")
 
# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
# The for loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set – you will learn about them soon) or other iterable objects (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        printprint(i)

# 2. You can use the break and continue statements to change the flow of a loop
text = "OpenEDG Python Institute
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
# You use continue to skip the current iteration, and continue with the next iteration
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
    
# 4. The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: range(start, stop, step), where:
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

##### Logical and Bitwise Operations
# 1. Python supports the following logical operators:

# and → if both operands are true, the condition is true, e.g., (True and True) is True,
# or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
# not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
# 2. You can use bitwise operators to manipulate single bits of data. The following sample data:

# x = 15, which is 0000 1111 in binary,
# y = 16, which is 0001 0000 in binary.
# will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
# ˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
# >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
# << does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

# ******************* Section 4. LISTS
# 4.1 Why do we need lists?
# It may happen that you have to read, store, process, and finally, print dozens, maybe hundreds, perhaps even thousands of numbers. What then? Do you need to create a separate variable for each value? Will you have to spend long hours writing statements like the one below?
# numbers = [10, 5, 7, 2, 1]
# The length of a list may vary during execution. New elements may be added to the list, while others may be removed from it. This means that the list is a very dynamic entity.
# If you want to check the list's current length, you can use a function named len() (its name comes from length).
# The function takes the list's name as an argument, and returns the number of elements currently stored inside the list (in other words ‒ the list's length)
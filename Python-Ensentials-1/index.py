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
# 4.3 Accessing list content
print(numbers[0]) # Accessing the list's first element.
# 4.6 Functions vs. methods
# A method is a specific kind of function ‒ it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.
# A function doesn't belong to any data ‒ it gets data, it may create new data and it (generally) produces a result.
# A method does all these things, but is also able to change the state of a selected entity.
# A method is owned by the data it works for, while a function is owned by the whole code.
# This also means that invoking a method requires some specification of the data from which the method is invoked.


# 4.7 Adding elements to a list: append() and insert()
# A new element may be glued to the end of the existing list:
# ******* list.append(value)
# Such an operation is performed by a method named append(). It takes its argument's value and puts it at the end of the list which owns the method.
# The list's length then increases by one.
# The insert() method is a bit smarter ‒ it can add a new element at any place in the list, not only at the end.
# list.insert(location, value)
# It takes two arguments:
# the first shows the required location of the element to be inserted; note: all the existing elements that occupy locations to the right of the new element (including the one at the indicated position) are shifted to the right, in order to make space for the new element;
# the second is the element to be inserted.

# ****** list.insert(location, value)

# You can start a list's life by making it empty (this is done with an empty pair of square brackets) and then adding new elements to it as needed.
# Take a look at the snippet in the editor. Try to guess its output after the for loop execution. Run the program to check if you were right.
my_list = []  # Creating an empty list.
for i in range(5):
    my_list.append(i + 1)

print(my_list)

# ********* 4.8 Making use of lists
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
# The second aspect of the for loop
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# ********    5.1 The bubble sort
# Increasing (or more precisely ‒ non-decreasing) ‒ if in every pair of adjacent elements, the former element is not greater than the latter;
# Decreasing (or more precisely ‒ non-increasing) ‒ if in every pair of adjacent elements, the former element is not less than the latter.

# 5.2 Sorting a list

# We solve this issue in the following way: we introduce another variable; its task is to observe if any swap has been done during the pass or not; if there is no swap, then the list is already sorted, and nothing more has to be done. We create a variable named swapped, and we assign a value of False to it, to indicate that there are no swaps. Otherwise, it will be assigned True.
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.
        
        

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)        

# If you want Python to sort your list, you can do it like this:

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# *******  6.1 The inner life of lists
# my_list[start:end]

# Note: not to end but to end - 1. An element with an index equal to end is the first element which does not take part in the slicing.
# Using negative values for both start and end is possible (just like in indexing).

# ***** 6.2 Powerful slices
# The new_list list will have end - start (3 - 1 = 2) elements ‒ the ones with indices equal to 1 and 2 (but not 3).
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# **** 6.3 Slices – negative indices

my_list[start:end]
# Start is the index of the first element included in the slice;
# End is the index of the first element not included in the slice.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list[:end] == my_list[0:end]
# Similarly, if you omit the end in your slice, it is assumed that you want the slice to end at the element with the index len(my_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# my_list[start:]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

# ****** 6.4 The in and not in operators

elem in my_list
elem not in my_list

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

# print(largest)  17

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)


vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']

# 2. If you want to copy a list or part of the list, you can do it by performing slicing:

colors = ['red', 'green', 'orange']
copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

# 3. You can use negative indices to perform slices, too. For example:
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# 4. The start and end parameters are optional when performing a slice: list[start:end], e.g.:
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

# 5. You can delete slices using the del instruction:
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

# 6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

# ******* 7.1 Lists in lists
# 1. List comprehension allows you to create new lists from existing ones in a concise and elegant way
# [expression for element in list if conditional]
# which is actually an equivalent of the following code:
for element in list:
    if conditional:
        expression
        
cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]

#********** SECTION 1 - FUNCTION ************
# It often happens that a particular piece of code is repeated many times in your program.
# If a particular fragment of the code begins to appear in more than one place, consider the possibility of isolating it in the form of a function invoked from the points where the original code was placed before

# You need to define it. The word define is significant here

# It always starts with the keyword def (for define)
# next after def goes the name of the function (the rules for naming functions are exactly the same as for naming variables)
# after the function name, there's a place for a pair of parentheses (they contain nothing here, but that will change soon)
# the line has to be ended with a colon;
# the line directly after def begins the function body ‒ a couple (at least one) of necessarily nested instructions, which will be executed every time the function is invoked; note: the function ends where the nesting ends, so you have to be careful.

def function_name():
    function_body

def message():
    print("Enter a value: ")

def message():
    print("Enter a value: ")

print("We start here.")
print("We end here.")

# We've modified the code now ‒ we've inserted the function's invocation between the start and end messages
def message():
    print("Enter a value: ")

print("We start here.")
message()
print("We end here.")

# 1. A function is a block of code that performs a specific task when the function is called (invoked). You can use functions to make your code reusable, better organized, and more readable. Functions can have parameters and return values.
# 2. There are at least four basic types of functions in Python:

# built-in functions which are an integral part of Python (such as the print() function). You can see a complete list of built-in Python functions at https://docs.python.org/3/library/functions.html.
# the ones that come from pre-installed modules (you'll learn about them in the Python Essentials 2 course)
# user-defined functions which are written by users for users ‒ you can write your own functions and use them freely in your code,
# the lambda functions (you'll learn about them in the Python Essentials 2 course.)
# 3. You can define your own function using the def keyword and the following syntax:

# def your_function(optional parameters):
#     # the body of the function

# You can define a function which doesn't take any arguments, e.g.:

def message(): # defining a function
    print("Hello") # body of the function

message() # calling the function


# You can define a function which takes arguments, too, just like the one-parameter function below:

def hello(name): # defining a function
    print("Hello,", name) # body of the function

name = input("Enter your name: ")

hello(name) # calling the function


# We'll tell you more about parametrized functions in the next section. Don't worry.

# **** 2.1 Parameterized functions
# The function's full power reveals itself when it can be equipped with an interface that is able to accept data provided by the invoker
# parameters exist only inside functions in which they have been defined, and the only place where the parameter can be defined is a space between a pair of parentheses in the def statement;
# assigning a value to the parameter is done at the time of the function's invocation, by specifying the corresponding argument.

# Don't forget:

# parameters live inside functions (this is their natural environment)
# arguments exist outside functions, and are carriers of values passed to corresponding parameters.

def message(number):
    print("Enter a number:", number)

def message(number):
    print("Enter a number:", number)

message(1)

def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

# 2.2 Positional parameter passing

# A technique which assigns the ith (first, second, and so on) argument to the ith (first, second, and so on) function parameter is called positional parameter passing, while arguments passed in this way are named positional arguments.
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

# 2.3 Keyword argument passing
# Python offers another convention for passing arguments, where the meaning of the argument is dictated by its name, not by its position ‒ it's called keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# 2.4 Mixing positional and keyword arguments
# You can mix both styles if you want ‒ there is only one unbreakable rule: you have to put positional arguments before keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)  #output: 1 + 2 + 3 = 6

# 1. You can pass information to functions by using parameters. Your functions can have as many parameters as you need
def hi(name):
    print("Hi,", name)

hi("Greg")

# An example of a two-parameter function:
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

# 2. You can pass arguments to a function using the following techniques:

# positional argument passing in which the order of arguments passed matters (Ex. 1)
# keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2)
# a mix of positional and keyword argument passing (Ex. 3.)

Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

# ***** 3.1 Effects and results: the return instruction

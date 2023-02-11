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
# To get functions to return a value (but not only for this purpose) you use the return instruction.
# 1. return without an expression
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
    
happy_new_year()
happy_new_year(False)	

# 2. return with an expression
def function():
    return expression

# There are two consequences of using it:

# it causes the immediate termination of the function's execution (nothing new compared to the first variant)
# moreover, the function will evaluate the expression's value and will return it (hence the name once again) as the function's result.

def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned its result. It's:", x)

# 3.2 A few words about None
# Note: None is a keyword.

# There are only two kinds of circumstances when None can be safely used:
# when you assign it to a variable (or return it as a function's result)
# when you compare it with a variable to diagnose its internal state.
value = None
if value is None:
    print("Sorry, you don't carry any value")

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))

# 3.3 Effects and results: lists and functions
# The first is: may a list be sent to a function as an argument?
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([5, 4, 3]))

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5)) #[4, 3, 2, 1, 0]

# 1. You can use the return keyword to tell a function to return some value. The return statement exits the function

def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

# 2. The result of a function can be easily assigned to a variable
def wishes():
    return "Happy Birthday!"
w = wishes()
print(w) # outputs: Happy Birthday!

# Look at the difference in output in the following two examples:
# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes() # outputs: My Wishes

# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
# Happy Birthday

# 3. You can use a list as a function's argument
def hi_everybody(my_list):
    for name in my_list:
   "woda": "water",
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])

# 4. A list can be a function result
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

# ******* 4.1 Functions and scopes
# 1. A variable that exists outside a function has scope inside the function body (Example 1) unless the function defines a variable of the same name (Example 2, and Example 3), e.g.:

# Example 1:

var = 2

def mult_by_var(x):
    return x * var

print(mult_by_var(7)) # outputs: 14


# Example 2:

def mult(x):
    var = 5
    return x * var

print(mult(7)) # outputs: 35


# Example 3:

def mult(x):
    var = 7
    return x * var

var = 3
print(mult(7)) # outputs: 49


# 2. A variable that exists inside a function has scope inside the function body (Example 4), e.g.:

# Example 4:

def adding(x):
    var = 7
    return x + var

print(adding(4)) # outputs: 11
print(var) # NameError


# 3. You can use the global keyword followed by a variable name to make the variable's scope global, e.g.:

var = 2
print(var) # outputs: 2

def return_var():
    global var
    var = 5
    return var

print(return_var()) # outputs: 5
print(var) # outputs: 5

# 5.1 Sample functions

def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65)) # 19.283746556473833

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))

def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))
# We've modified the code a bit:
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(6))

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.4535923

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) # 27.565214082533313

# 5.2 Sample functions: Triangles
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# This is a more compact version
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
# Can we compact it even more?
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
    

# 5.3 Sample functions: Factorials
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorial_function(n))
    
    
# 5.4 Fibonacci numbers
# They are a sequence of integer numbers built using a very simple rule:
# the first element of the sequence is equal to one (Fib1 = 1)
# the second is also equal to one (Fib2 = 1)
# every subsequent number is the the_sum of the two preceding numbers:(Fibi = Fibi-1 + Fibi-2)

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))
    
# 5.5 Recursion
# In this field, recursion is a technique where a function invokes itself.
# Fibi = Fibi-1 + Fibi-2
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
# The factorial has a second, recursive side too
# n! = (n-1)! × n
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))
    
# ********* SECTION 6 - TUPLES AND DICTIONARIES **********

# ** 6.2 Tuples
# A tuple is an immutable sequence type
# tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas
# How to create a tuple
empty_tuple = ()
my_tuple = (1, 10, 100, 1000)
for elem in my_tuple:
    print(elem)
    
#What else can tuples do for you?

# the len() function accepts tuples, and returns the number of elements contained inside;
# the + operator can join tuples together (we've shown you this already)
# the * operator can multiply tuples, just like lists;
# the in and not in operators work in the same way as in lists

# ** 6.3 Dictionaries
# It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable
# The list of pairs is surrounded by curly braces, while the pairs themselves are separated by commas, and the keys and values by colons
# In Python's world, the word you look for is named a key. The word you get from the dictionary is called a value.

# This means that a dictionary is a set of key-value pairs. Note:
# each key must be unique − it's not possible to have more than one key of the same value;
# a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
# a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
# the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
# a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# The keys() method
# Can dictionaries be browsed using the for loop, like lists or tuples?
# No and yes.
# No, because a dictionary is not a sequence type − the for loop is useless with it.

# The first of them is a method named keys(), possessed by each dictionary. The method returns an iterable object consisting of all the keys gathered within the dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
# The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

# The sorted() function
for key in sorted(dictionary.keys()):
# There is also a method called values(), which works similarly to keys(), but returns values.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

# 6.5 Tuples and dictionaries can work together
# Let's imagine the following problem:

# you need a program to evaluate the students' average scores;
# the program should ask for the student's name, followed by her/his single score;
# the names may be entered in any order;
# entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise the ValueError exception, but don't worry about that now, you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
# a list of all names, together with the evaluated average score, should be then emitted.

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):    
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

# line 1: create an empty dictionary for the input data; the student's name is used as a key, while all the associated scores are stored in a tuple (the tuple may be a dictionary value - that's not a problem at all)
# line 3: enter an "infinite" loop (don't worry, it'll break at the right moment)
# line 4: read the student's name here;
# line 5-6: if the name is an empty string (), leave the loop;
# line 8: ask for one of the student's scores (an integer from the range 0-10)
# line 9-10: if the score entered is not within the range from 0 to 10, leave the loop;
# line 12-13: if the student's name is already in the dictionary, lengthen the associated tuple with the new score (note the += operator)
# line 14-15: if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score;
# line 17: iterate through the sorted students' names;
# line 18-19: initialize the data needed to evaluate the average (sum and counter)
# line 20-22: we iterate through the tuple, taking all the subsequent scores and updating the sum, together with the counter;
# line 23: evaluate and print the student's name and average score.

# 1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists.
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)
my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

# 2. You can create an empty tuple like this:
empty_tuple = ()
print(type(empty_tuple)) # outputs:
# 3. A one-element tuple may be created as follows:
one_elem_tuple_1 = ("one", ) # Brackets and a comma.
one_elem_tuple_2 = "one", # No brackets, just a comma.
# 1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data.
# Each dictionary is a set of key: value pairs.
my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}

# ******* SECTION 7 - EXCEPTIONS **********
# 7.3 The try-except branch
# You can see two branches here:
# first, starting with the try keyword – this is the place where you put the code you suspect is risky and may be terminated in case of error; note: this kind of error is called an exception, while the exception occurrence is called raising – we can say that an exception is (or was) raised;
# second, the part of the code starting with the except keyword is designed to handle the exception; it's up to you what you want to do here: you can clean up the mess or you can just sweep the problem under the carpet (although we would prefer the first solution).
# So, we could say that these two blocks work like this:
# the try keyword marks the place where you try to do something without permission;
# the except keyword starts a location where you can show off your apology talents.
try:
	# It's a place where
	# you can do something 
    # without asking for permission.
except:
	# It's a spot dedicated to 
    # solemnly begging for forgiveness.
    
# 7.4 The exception proves the rule
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
    
# any part of the code placed between try and except is executed in a very special way – any error which occurs here won't terminate program execution. Instead, the control will immediately jump to the first line situated after the except keyword, and no other part of the try branch is executed;
# the code in the except branch is activated only when an exception has been encountered inside the try block. There is no way to get there by any other means;
# when either the try block or the except block is executed successfully, the control returns to the normal path of execution, and any code located beyond in the source file is executed as if nothing happened.
# Now we want to ask you an innocent question: is ValueError the only way the control could fall into the except branch?

# Two exceptions after one try
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
    
# 7.6 The default exception and how to use it
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
    
# 7.7 Some useful exceptions
# 1. ZeroDivisionError
# This appears when you try to force Python to perform any operation which provokes division in which the divider is zero, or is indistinguishable from zero. Note that there is more than one Python operator which may cause this exception to raise. Can you guess them all?
# Yes, they are: /, //, and %.
# 2.ValueError
# Expect this exception when you're dealing with values which may be inappropriately used in some context. In general, this exception is raised when a function (like int() or float()) receives an argument of a proper type, but its value is unacceptable.
# 3. TypeError
# This exception shows up when you try to apply a data whose type cannot be accepted in the current context.
# 4. AttributeError
# This exception arrives – among other occasions – when you try to activate a method which doesn't exist in an item you're dealing with.
# 5. SyntaxError
# This exception is raised when the control reaches a line of code which violates Python's grammar. It may sound strange, but some errors of this kind cannot be identified without first running the code

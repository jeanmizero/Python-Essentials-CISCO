# **** MODULES  *****
# 1.1 What is a module?
# 1.3 Importing a module
# The clause contains:
# the import keyword;
# the name of the module which is subject to import.
# import math
# import math
# import sys
# import math, sys

# It's simple, you put:
# the name of the module (e.g., math)
# a dot (i.e., .)
# the name of the entity (e.g., pi)
import math

print(math.sin(math.pi / 2))


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi / 2))
print(math.sin(math.pi / 2))

# In the second method, the import's syntax precisely points out which module's entity (or entities) are acceptable in the code:
# from math import pi
# The instruction consists of the following elements:

# the from keyword;
# the name of the module to be (selectively) imported;
# the import keyword;
# the name or list of names of the entity/entities which are being imported into the namespace.
# The instruction has this effect:

# the listed entities (and only those ones) are imported from the indicated module;
# the names of the imported entities are accessible without qualification.

from math import sin, pi

print(sin(pi / 2))

# 1.6 Importing a module: *
# Such an instruction imports all entities from the indicated module.
from module import *

# Is it convenient? Yes, it is, as it relieves you of the duty of enumerating all the names you need.
# Is it unsafe? Yes, it is - unless you know all the names provided by the module, you may not be able to avoid name conflicts

# PACKAGE INSTALLER(PIP)
# 4.3 How to install pip
# The question that should be put now is: how to get a proper cheese knife? In other words, how to ensure that pip is installed and ready to work?
# The most precise answer is “it depends”. Really.
# Some Python installations come with pip, some don't. What’s more, it doesn’t only depend on the OS you use, although this is a very important factor.

# pip on MS Windows
pip - -version
# pip on Linux

pip - -version
# Unfortunately, some Linux distributions don't have pip preinstalled, even if Python itself is installed by default (some versions of Ubuntu may behave this way). In this case, you have two possibilities:
# install pip as a system package using a dedicated package manager (e.g., apt in Debian-like systems)
# install pip using internal Python mechanisms
pip3 - -version
# If you're a Mac user and you've installed Python 3 using the brew installer, pip is already present in your system and ready to work.
pip3 - -version
# 4.5 How to use pip
pip help
pip help operation
pip help install
pip list

# 4.7 Use pip!
# Pip's capabilities don't end here, but the command set we've presented to you is enough to start successfully managing packages that aren't a part of the regular Python installation.
# We hope we’ve encouraged you to carry out your own experiments with pip and the Python package universe. PyPI invites you to dive into its extensive resources.
# Some say that one of the most important programming virtues is laziness. Don't get us wrong – we don't want you to spend all day napping on the couch and dreaming of Python code.
# A lazy programmer is a programmer who looks for existing solutions and analyzes the available code before they start to develop their own software from scratch.
# This is why PyPI and pip exist – use them!

# 4. The list of the main pip activities looks as follows:

# pip help operation – shows a brief description of pip;
# pip list – shows a list of the currently installed packages;
# pip show package_name – shows package_name info including the package's dependencies;
# pip search anystring – searches through PyPI directories in order to find packages whose names contain anystring;
# pip install name – installs name system-wide (expect problems when you don't have administrative rights);
# pip install --user name – installs name for you only; no other platform user will be able to use it;
# pip install -U name – updates a previously installed package;
# pip uninstall name – uninstalls a previously installed package.

# ******* SECTION 1 - CHARACTERS AND STRINGS VS COMPUTERS *******
# 1. Computers store characters as numbers. There is more than one possible way of encoding characters, but only some of them gained worldwide popularity and are commonly used in IT: these are ASCII (used mainly to encode the Latin alphabet and some of its derivates) and UNICODE (able to encode virtually all alphabets being used by humans).
# 2. A number corresponding to a particular character is called a codepoint.
# 3. UNICODE uses different ways of encoding when it comes to storing the characters using files or computer memory: two of them are UCS-4 and UTF-8 (the latter is the most common as it wastes less memory space).

# 2.1 Strings - a brief review
word = 'by'
print(len(word))
# 2.4 Strings as sequences
# Indexing
# We told you before that Python strings are sequences. It's time to show you what that actually means.
# Strings aren't lists, but you can treat them like lists in many particular cases.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()
# 2.5 Slices
# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# 2.6 The in and not in operators
# The in operator
# The in operator shouldn't surprise you when applied to strings – it simply checks if its left argument (a string) can be found anywhere within the right argument (another string).
# The result of the check is simply True or False.
# Look at the example program below. This is how the in operator works:

# The not in operator
# As you probably suspect, the not in operator is also applicable here.
# This is how it works

# 2.7 Python strings are immutable
# 3. Strings can be concatenated using the + operator, and replicated using the * operator. For example:
asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)

# The count() method
# The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't cause any problems
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# 3.4 The find() method
# The find() method is similar to index(), which you already know – it looks for a substring and returns the index of the first occurrence of this substring, but:
# it's safer – it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
# it works with strings only – don't try to apply it to any other sequence

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

# 3.5 The isalnum() method
# The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# 3.6 The isalpha() method
# The isalpha() method is more specialized – it's interested in letters only.
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# 3.7 The isdigit() method
# In turn, the isdigit() method looks at digits only – anything else produces False as the result.
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

# 3.8 The islower() method
# The islower() method is a fussy variant of isalpha() – it accepts lower-case letters only.
# Example: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# 3.9 The isspace() method
# The isspace() method identifies whitespaces only – it disregards any other character (the result is False then).
# Example: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# 3.11 The join() method
# The join() method is rather complicated, so let us guide you through it step by step:

# as its name suggests, the method performs a join – it expects one argument as a list; it must be assured that all the list's elements are strings – the method will raise a TypeError exception otherwise;
# all the list's elements will be joined into one string but...
# ...the string from which the method has been invoked is used as a separator, put among the strings;
# the newly created string is returned as a result
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# 3.12 The lower() method
# The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts, and returns the string as the result.
# Note: The lower() method doesn't take any parameters.
# Demonstrating the lower() method:
print("SiGmA=60".lower())

# 3.13 The lstrip() method
# The parameterless version of the lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))

# 3.14 The replace() method
# The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# 3.17 The split() method
# The split() method does what it says – it splits the string and builds a list of all detected substrings.
# The method assumes that the substrings are delimited by whitespaces – the spaces don't take part in the operation, and aren't copied into the resulting list
# Demonstrating the split() method:
print("phi       chi\npsi".split())

# 1. Some of the methods offered by strings are:

# capitalize() – changes all string letters to capitals;
# center() – centers the string inside the field of a known length;
# count() – counts the occurrences of a given character;
# join() – joins all items of a tuple/list into one string;
# lower() – converts all the string's letters into lower-case letters;
# lstrip() – removes the white characters from the beginning of the string;
# replace() – replaces a given substring with another;
# rfind() – finds a substring starting from the end of the string;
# rstrip() – removes the trailing white spaces from the end of the string;
# split() – splits the string into a substring using a given delimiter;
# strip() – removes the leading and trailing white spaces;
# swapcase() – swaps the letters' cases (lower to upper and vice versa)
# title() – makes the first letter in each word upper-case;
# upper() – converts all the string's letter into upper-case letters.

# 2. String content can be determined using the following methods (all of them return Boolean values):

# endswith() – does the string end with a given substring?
# isalnum() – does the string consist only of letters and digits?
# isalpha() – does the string consist only of letters?
# islower() – does the string consists only of lower-case letters?
# isspace() – does the string consists only of white spaces?
# isupper() – does the string consists only of upper-case letters?
# startswith() – does the string begin with a given substring?

# 4.1 Comparing strings
# 4.2 Sorting
# Comparing is closely related to sorting (or rather, sorting is in fact a very sophisticated case of comparing).
# This is a good opportunity to show you two possible ways to sort lists containing strings. Such an operation is very common in the real world – any time you see a list of names, goods, titles, or cities, you expect them to be sorted.
# The first is implemented as a function named sorted().
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()


# 1. An exception is an event during program execution caused by an abnormal situation. The exception should he handled to avoid the termination of the program. The part of your code that is suspected of being the source of the exception should be put inside the try branch.

# When the exception happens, the execution of the code is not terminated, but instead jumps into the except branch. This is the place where the handling of the exception should take place. The general scheme for such a construction looks as follows:

# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except:
    :
    # Crisis management takes place here.
    :
:
# Back to normal.
:


# 2. If you need to handle more than one exception coming from the same try branch, you can add more than one except branch, but you have to label them with different exception names, like this:

# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
:
# Back to normal.
:


# At most, one of the except branches is executed – none of the branches is performed when the raised exception doesn't match any of the specified exceptions.

# 3. You cannot add more than one anonymous (unnamed) except branch after the named ones.

# The code that always runs smoothly.
:
try:
    :
    # Risky code.
    :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
except:
    # All other issues fall here.
:
# Back to normal.
:




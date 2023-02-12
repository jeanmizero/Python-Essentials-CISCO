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


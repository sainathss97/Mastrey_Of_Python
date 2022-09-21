##***What is a Module?***

Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

##***What is a Package?***

A directory which can hold multiple modules of a project including `__init__.py` which tells the intrepter that this is a package not a module.

##***How and when to use `import` ?***

1.we use it to import modules
        `import shopping_cart`
    
2.we use it to import packages
        `import shopping.shopping_cart` for a module in a package we use `.` operators
        `import shopping.more_shopping.shopping_cart` for a module inside a package inside a package

## ***How to use `from ... import ...` ?***

This is a cleaner way to import files without using log `.` operators
    1. `from shopping.more_shopping.shopping_cart import buy`  # for a specific functions that are needed to import 
    2. `from shopping.more_shopping.shopping_cart import *`  # for all methods in a module 
##**What is the use `__name__` in modules and packages ?**
[resource](https://www.tutorialspoint.com/name-a-special-variable-in-python)

Unlike other programming languages, python is not designed to start execution of the code from a main function explicitly. 
A special variable called __name__ provides the functionality of the main function. 
As it is an in-built variable in python language, we can write a program just to see the value of this variable as below.

1. When you run any well-written stand-alone python script which is not referring to any other script, the value of __name__ variable is equal to __main__.

Let's write a program named standalone.py to illustrate this feature.
```
def func1():
   print 'The value of __name__ is ' + __name__
if __name__ == '__main__':
   func1()
```
Running the above code gives us the following result −

The value of __name__ is __main__
As expected the __name__ variable evaluates to __main__ hence the output.

2. The second feature is about importing one python script into another. In such a scenario, there seem to be two different scopes which can be considered as the main() function. 
 The first scope can be the __main__ variable of the currently running program and the second the scope of the __main__ variable of the imported script used in the current program.

So which __main__ variable will be used 

when you run a function from the imported script, the __name__ variable will evaluate to the actual name of the script and not equal to __main__.

But when you find out the value of the name variable from the current program, without referring to the imported script, it will evaluate to __main__ as expected, as that is the scope of the program at level 0 indention.

## **How to check for built in Methods for Python?**
[resource:](https://docs.python.org/3/) Python Docs are the best way alternatively we can use
[ask python](https://www.askpython.com)


## **Are any Packages available apart from the default modules?**

Yes you can, you should learn about [PYPI](https://pypi.org)
install them with pip installer 



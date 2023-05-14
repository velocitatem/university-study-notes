programming
# Data Types


<a id="org8a0d9c7"></a>

## Integers

An integer is a whole number, positive or negative, with no fractional part.
In python integers are represented by the int class. The int class has the following methods:

-   `__add__(self, other)__` : returns the sum of self and other
-   `__sub__(self, other)__` : returns the difference of self and other
-   `__mul__(self, other)__` : returns the product of self and other
-   `__floordiv__(self, other)__` : returns the quotient of self and other
-   `__mod__(self, other)__` : returns the remainder of self and other
-   `__pow__(self, other)__` : returns the power of self and other
-   `__abs__(self)__` : returns the absolute value of self
-   `__neg__(self)__` : returns the negative value of self
-   `__pos__(self)__` : returns the positive value of self

How do we use integers in python?

    a = 5
    b = 2
    print(a.__add__(b))
    print(a+b)

    7
    7


<a id="org4955a02"></a>

## Floating Point Numbers

A floating point number is a number with a fractional part. In python floating point numbers are represented by the float class. The float class has the following methods:

-   `__add__(self, other)__` : returns the sum of self and other
-   `__sub__(self, other)__` : returns the difference of self and other
-   `__mul__(self, other)__` : returns the product of self and other
-   `__floordiv__(self, other)__` : returns the quotient of self and other
-   `__mod__(self, other)__` : returns the remainder of self and other
-   `__pow__(self, other)__` : returns the power of self and other
-   `__abs__(self)__` : returns the absolute value of self
-   `__neg__(self)__` : returns the negative value of self
-   `__pos__(self)__` : returns the positive value of self

The difference between the int and float classes is that the float class has the following methods:

-   `__truediv__(self, other)__` : returns the quotient of self and other
-   `__round__(self, ndigits)__` : returns the rounded value of self to ndigits decimal places
-   `__floor__(self)__` : returns the floor value of self
-   `__ceil__(self)__` : returns the ceiling value of self

How do we use floating point numbers in python?

    a = 5.0
    b = 2.0
    c = 2.5128596
    print(a.__truediv__(b))
    print(a/b)
    print(c.__round__(3))

    2.5
    2.5
    2.513


<a id="org92b912b"></a>

## Strings

A string is a sequence of characters. In python strings are represented by the str class. The str class has the following methods:

-   `__add__(self, other)__` : returns the concatenation of self and other
-   `__mul__(self, other)__` : returns the product of self and other
-   `__len__(self)__` : returns the length of self
-   `__getitem__(self, key)__` : returns the character at index key of self
-   `__setitem__(self, key, value)__` : sets the character at index key of self to value
-   `__delitem__(self, key)__` : deletes the character at index key of self
-   `__contains__(self, item)__` : returns True if item is in self, False otherwise
-   `__iter__(self)__` : returns an iterator over self
-   `__reversed__(self)__` : returns a reversed iterator over self
-   `__eq__(self, other)__` : returns True if self and other are equal, False otherwise
-   `__ne__(self, other)__` : returns True if self and other are not equal, False otherwise
-   `__lt__(self, other)__` : returns True if self is less than other, False otherwise
-   `__le__(self, other)__` : returns True if self is less than or equal to other, False otherwise
-   `__gt__(self, other)__` : returns True if self is greater than other, False otherwise
-   `__ge__(self, other)__` : returns True if self is greater than or equal to other, False otherwise
-   `__hash__(self)__` : returns the hash value of self
-   `__str__(self)__` : returns the string representation of self
-   `__repr__(self)__` : returns the string representation of self
-   `__format__(self, format_spec)__` : returns the formatted string representation of self

How do we use strings in python? We can use single quotes or double quotes to represent strings.

    a = 'Hello'
    b = "World"
    # here are some examples of string methods
    print(a.__add__(b))
    print(a.__hash__())
    print(a.__len__())
    print(a.__getitem__(1))
    print(b.__contains__('l'))

    HelloWorld
    -705289849546263557
    5
    e
    True


<a id="orga68222e"></a>

## Booleans

A boolean is a value that can be either True or False. In python booleans are represented by the bool class. The bool class has the following methods:

-   `__and__(self, other)__` : returns the logical and of self and other
-   `__or__(self, other)__` : returns the logical or of self and other
-   `__xor__(self, other)__` : returns the logical xor of self and other
-   `__eq__(self, other)__` : returns True if self and other are equal, False otherwise
-   `__ne__(self, other)__` : returns True if self and other are not equal, False otherwise
-   `__hash__(self)__` : returns the hash value of self
-   `__str__(self)__` : returns the string representation of self
-   `__repr__(self)__` : returns the string representation of self

How do we use booleans in python?

    a = True
    b = False
    print(a.__and__(b))
    print(a.__or__(b))
    print(a.__xor__(b))
    print(a.__hash__())

    False
    True
    True
    1

Another way we can use booleans in python is by using the following operators:

-   `and` : returns the logical and of two values
-   `or` : returns the logical or of two values
-   `not` : returns the logical not of a value

Examples:

    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not a)

    False
    True
    False

We will also introduce more in coming sections.


<a id="orgc812eb2"></a>

# Flow Control Statements


<a id="orgb8d4a6a"></a>

## Conditional Statements

Conditional statements are used to control the flow of execution of a program. In python conditional statements are represented by the if, elif, and else statements. The syntax of the if statement is as follows:

    if condition:
      # do something
      print('Hello')

If we need to use multiple conditions we can use the elif statement. The syntax of the elif statement is as follows:

    if condition1:
      # do something
      print('Hello')
    elif condition2:
      # do something
      print('World')

If none of the conditions are met we can use the else statement. The syntax of the else statement is as follows:

    if condition1:
      # do something
      print('Hello')
    elif condition2:
      # do something
      print('World')
    else:
      # do something
      print('!')


<a id="org58f827c"></a>

## Loops

Loops are used to repeat a block of code. In python loops are represented by the for and while statements. The syntax of the for statement is as follows:

    for i in range(10):
      # do something
      print(i)

We can also make looks more interesting by using the following syntax:

    someList = [x for x in range(10)]
    print(someList)

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

We call this a list comprehension. We can also use list comprehensions to create lists of lists. The general syntax of a list comprehension is as follows:

`[[expression] for item in iterable if condition]`


### While

The syntax of the while statement is as follows:

    i = 0
    while i < 10:
      # do something
      print(i)
      i += 1


<a id="orgd547ee5"></a>

## Break and Continue

The break statement is used to exit a loop. The continue statement is used to skip the current iteration of a loop. The syntax of the break statement is as follows:

    for i in range(10):
      if i == 5:
        break
      print(i)

    0
    1
    2
    3
    4

The syntax of the continue statement is as follows:

    for i in range(10):
      if i == 5:
        continue
      print(i)

    0
    1
    2
    3
    4
    6
    7
    8
    9

We can see that the number 5 is not printed because we used the continue statement to skip the current iteration of the loop.


<a id="orga485dd7"></a>

# Logic


<a id="orgdfcde22"></a>

## Truth Value Testing

In python we can test the truth value of an object. The following values are considered false:

-   `None`
-   `False`
-   `zero of any numeric type`
-   `any empty sequence, for example, '', (), []`
-   `any empty mapping, for example, {}`

All other values are considered true. For example:

-   `True`
-   `non-zero numbers`
-   `non-empty strings`
-   `non-empty lists`
-   `non-empty tuples`
-   `non-empty dictionaries`

We can use the following functions to test the truth value of an object:

-   `bool()` : returns the truth value of an object
-   `all()` : returns True if all elements of an iterable are true (or if the iterable is empty)
-   `any()` : returns True if any element of an iterable is true. If the iterable is empty, returns False


<a id="org83a2da9"></a>

## Identity Operators

The identity operators are used to compare the memory locations of two objects. The identity operators are:

-   `is` : returns True if the operands are identical (refer to the same object)
-   `is not` : returns True if the operands are not identical (do not refer to the same object)

Examples:

    a = 5
    b = 5
    print(a is b)
    print(a is not b)

    True
    False


<a id="orgc80e922"></a>

## Membership Operators

The membership operators are used to test whether a value or variable is found in a sequence. The membership operators are:

-   `in` : returns True if a sequence with the specified value is present in the object
-   `not in` : returns True if a sequence with the specified value is not present in the object

Examples:

    a = [1, 2, 3, 4, 5]
    print(1 in a)
    print(6 in a)
    print(1 not in a)
    print(6 not in a)

    True
    False
    False
    True


<a id="orgac813b4"></a>

## Bitwise Operators

Bitwise operators are used to compare (binary) numbers. The bitwise operators are:

-   `&` : binary and
-   `|` : binary or
-   `~` : binary xor
-   `~` : binary ones complement
-   `<<` : binary left shift
-   `>>` : binary right shift

Examples:

    a = 60
    b = 13
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(~a)
    print(a << 2)
    print(a >> 2)

    12
    61
    49
    -61
    240
    15

We probably won't use bitwise operators very often, but it's good to know they exist.


<a id="orgb8b5a58"></a>

# Scope and Constants


<a id="orgb612229"></a>

## Scope

Scope, is the area of a program where an object or name may be accessible. In python there are two types of scope:

-   `global` : a name that is defined outside of a function
-   `local` : a name that is defined inside a function

We can access a global variable inside a function by using the `global` keyword. The syntax of the `global` keyword is as follows: `global variableName`. For example:

    a = 5
    def myFunction():
      global a
      a = 10
      print(a)
    myFunction()
    print(a)

    10
    10


<a id="org9144fea"></a>

## Constants

Constants are variables whose value cannot be changed. In python constants are usually defined in all capital letters. For example: `PI`, `E`, `G`.

    PI = 3.14
    E = 2.71
    G = 9.81
    print(PI)
    print(E)
    print(G)

    3.14
    2.71
    9.81

What if we try to modify a constant? Let's try it:

    PI = 3.14
    PI = 3.15
    print(PI)

    3.15

We can see that we can modify a constant. This is because python does not have a constant type. We can use the `const` module to define constants. Python uses constants more as a semantic convention than a language feature. The `const` module is not part of the standard library, so we need to install it. We can install the `const` module using the `pip` command:


<a id="org2b1a508"></a>

# Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. In python a function is defined using the `def` keyword. The syntax of a function is as follows:

    def myFunction():
      print("Hello World")

We can call the function by using the function name followed by parenthesis. For example:

    myFunction()

    Hello World


<a id="org2081cf8"></a>

## Arguments

Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma. The following example has a function with one argument ( `name` ). When the function is called, we pass along a first name, which is used inside the function to print the full name:

    def myFunction(name):
      print(name + " Smith")
    myFunction("John")
    myFunction("Jane")
    myFunction("Joe")

    John Smith
    Jane Smith
    Joe Smith

We can also use default arguments. Default arguments are used when we call the function without arguments. For example:

    def myFunction(name = "John"):
      print(name + " Smith")
    myFunction()
    myFunction("Jane")
    myFunction("Joe")

    John Smith
    Jane Smith
    Joe Smith

These might also be called optional arguments.


<a id="org82c7a5e"></a>

## Return Types

To let a function return a value, use the `return` statement:

    def myFunction(x):
      return 5 * x
    print(myFunction(3))
    print(myFunction(5))
    print(myFunction(9))

    15
    25
    45

That is not the only way to get some data from a function, we can make use of `yield` statements. The `yield` statement is used to define a generator, which is covered in the next sections.


<a id="org0918f57"></a>

## Recursion

Python also accepts function recursion, which means a defined function can call itself. Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

Example:

    def fib(n):
      if n <= 1:
        return n
      else:
        return(fib(n-1) + fib(n-2))
    print(fib(7))

Be careful, python has a default recursion limit of 1000. If you need to increase the recursion limit, you can use the `sys.setrecursionlimit()` method. But this probably means you are doing something wrong.


<a id="orgfb7fa4c"></a>

# Lists

Probably the best datatype in python is the `list`. A list is a collection which is ordered and changeable. In python lists are written with square brackets. For example: `myList = [1, 2, 3]`. We can access the items of a list by referring to the index number. For example:

    myList = ["apple", "banana", "cherry"]
    print(myList[1])

    banana

We can also use negative indexing. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc. For example:

    myList = ["apple", "banana", "cherry"]
    print(myList[-1])

    cherry

Some important list methods are:

-   `append()` : adds an element at the end of the list
-   `clear()` : removes all the elements from the list
-   `copy()` : returns a copy of the list
-   `count()` : returns the number of elements with the specified value. Ex: `myList.count("apple")`
-   `extend()` : add the elements of a list (or any iterable), to the end of the current list. Ex: `myList.extend(myList2)`
-   `index()` : returns the index of the first element with the specified value
-   `insert()` : adds an element at the specified position. Ex: `myList.insert(2, "orange")`
-   `pop()` : removes the element at the specified position. This also returns the removed element. Ex: `myList.pop(1)`
-   `remove()` : removes the first item with the specified value. Ex: `myList.remove("banana")`
-   `reverse()` : reverses the order of the list
-   `sort()` : sorts the list


<a id="org80a14bb"></a>

## List Comprehension

This is really what makes python so powerful. List comprehension is an elegant way to define and create lists based on existing lists. For example:

    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    newList = [x for x in myList if x % 2 == 0]
    print(newList)

    [2, 4, 6, 8, 10]

This, is frankly amazing. We can also use `if` and `else` statements in list comprehension.

Here is an example of bad 'non-pythonic' code and how we can make it better using list comprehension:

1.  Example

    Bad code:

        myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        newList = []
        for x in myList:
          if x % 2 == 0:
            newList.append(x)
        print(newList)

        [2, 4, 6, 8, 10]

    Good Code:

        myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        newList = [x for x in myList if x % 2 == 0]
        print(newList)

        [2, 4, 6, 8, 10]

2.  Example 2

    Bad code:

        import random
        random.seed(1)
        myList = []
        for i in range(10):
          myList.append(random.randint(1, 100))
        print(myList)

        [18, 73, 98, 9, 33, 16, 64, 98, 58, 61]

    Good code:

        import random
        random.seed(1)
        myList = [random.randint(1, 100) for i in range(10)]
        print(myList)

        [18, 73, 98, 9, 33, 16, 64, 98, 58, 61]


<a id="orga3123b3"></a>

# Tuples

A tuple is a collection which is ordered and unchangeable. In python tuples are written with round brackets. For example: `myTuple = (1, 2, 3)`. We can access the items of a tuple by referring to the index number. For example:

    myTuple = ("apple", "banana", "cherry")
    print(myTuple[1])

    banana

It is somewhat like a list but immutable (cannot be changed). We can also use negative indexing. A very common way of using tuples is to return multiple values from a function. For example:

    def myFunction():
      return (1, 2, 3)
    print(myFunction())


<a id="org80d58af"></a>

# Spread Syntax

Spread syntax is a very powerful way of unpacking iterables. For example:

    myList = [1, 2, 3, 4, 5]
    print(*myList)

    1 2 3 4 5

Why is this useful? Well, we can use this to unpack a list into a function. For example:

    def myFunction(a, b, c, d, e):
      print(a, b, c, d, e)
    myList = [1, 2, 3, 4, 5]
    myFunction(*myList)

    1 2 3 4 5


<a id="org0c53b3b"></a>

## Dictionaries

We can step this up a notch by applying it to dicionaries. For example:

    myDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print(*myDict)

    a b c d e

This will print the keys of the dictionary. We can also use the `**` operator to unpack the values of the dictionary. For example:

    myDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    def myFunction(a, b, c, d, e):
      print(a, b, c, d, e)
    myFunction(**myDict)

    1 2 3 4 5


<a id="orgca4ade7"></a>

# Files

We can open a file using the `open()` function. The `open()` function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file:

-   `r` : Read - Default value. Opens a file for reading, error if the file does not exist
-   `a` : Append - Opens a file for appending, creates the file if it does not exist
-   `w` : Write - Opens a file for writing, creates the file if it does not exist
-   `x` : Create - Creates the specified file, returns an error if the file exists

Here is an example of how to open a file:

    myFile = open("myfile.txt")
    print(myFile.read())

    some data

The best practice is to use the `with` keyword when dealing with file objects. This has the advantage that the file is properly closed after its suite finishes, even if an exception is raised at some point.

    with open("myfile.txt") as myFile:
      print(myFile.read())

    some data

Key methods for file objects:

-   `read()` : reads the entire file
-   `readline()` : reads a single line
-   `readlines()` : reads all the lines into a list
-   `write()` : writes to the file
-   `close()` : closes the file


<a id="org9d2fe4d"></a>

## Writing to a file

How do we write to a file? We can use the `write()` method. For example:

    with open("myfile.txt", "w") as myFile:
      myFile.write("\nsome data")


<a id="org0a4d8b0"></a>

# GUI

We use the `graphics.py` library to create a GUI. We can create a window, draw shapes, and add text. You can find the documentation for the library [here](./graphics.pdf). Here is some key documentation for the library:

-   `GraphWin(title, width, height)` : creates a window
-   `Point(x, y)` : creates a point.
-   `Circle(center, radius)` : creates a circle, the center is a point.
-   `Rectangle(p1, p2)` : creates a rectangle. The points are the top left and bottom right corners, both are points.
-   `Line(p1, p2)` : creates a line. The points are the start and end points, both are points.
-   `Text(p, text)` : creates text. The point is the top left corner of the text.

Some key methods for the objects.

-   `.draw(win)` : draws the shape on the window. This is a method for all shapes.
-   `.setFill(color)` : sets the fill color of the shape. This is a method for all shapes.
-   `.setOutline(color)` : sets the outline color of the shape. This is a method for all shapes.
-   `.setText(text)` : sets the text of the text object. This is a method for the text object.
-   `.setFace(face)` : sets the face of the text object. This is a method for the text object.

Methods for the window:

-   `.getMouse()` : waits for a mouse click and returns the point where the mouse was clicked.
-   `.getKey()` : waits for a key press and returns the key that was pressed.
-   `.close()` : closes the window.

Here is an example of how to create a window and draw a circle:

    from graphics import *
    win = GraphWin("My Window", 500, 500)
    circle = Circle(Point(250, 250), 50)
    circle.draw(win)
    win.getMouse()
    win.close()


<a id="orgb8bde26"></a>

# OOP

OOP might shake things up a bit, but it only makes things easier in the end. We can create classes and objects. We can also create methods and attributes. Here is an example of how to create a class:

    class MyClass:
      def __init__(self, name):
        self.name = name
      def myMethod(self):
        print("Hello, my name is " + self.name)
    myObject = MyClass("John")
    myObject.myMethod()

Might look intimidating at first, but it's not that bad. Let's break it down. Classes have a very specific syntax. We start with the `class` keyword, followed by the name of the class. We then have a colon.

The body of the class is where we define the methods and attributes of the class. We can define methods using the `def` keyword. Each method must have the `self` parameter. The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

It is important to now the methods with a `__` prefix. These are special methods. The `__init__` method is a constructor, which is called when the class is being initiated. The `__init__` method is called automatically every time the class is being used to create a new object. Other methods:

-   `__del__` : destructor, called when the object is about to be destroyed
-   `__repr__` : returns a string representation of the object
-   `__str__` : returns a string representation of the object
-   `__add__` : defines behavior for the + operator
-   `__sub__` : defines behavior for the - operator
-   `__mul__` : defines behavior for the \* operator
-   `__truediv__` : defines behavior for the / operator
-   `__mod__` : defines behavior for the % operator
-   `__lt__` : defines behavior for the < operator
-   `__le__` : defines behavior for the <= operator
-   `__eq__` : defines behavior for the == operator
-   `__ne__` : defines behavior for the != operator
-   `__gt__` : defines behavior for the > operator
-   `__ge__` : defines behavior for the >= operator

With these methods, we can make life easier by defining them for our object, so that when we want to add two objects, we can just use the + operator, instead of having to define a method for it.


<a id="org0a2a9ed"></a>

## Inheritance

Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important terminology:

-   `Superclass` : a class from which we derive from
-   `Subclass` : a class that we derive from another class

The benefits of inheritance are:

-   It represents real-world relationships well
-   It provides reusability of a code
-   It allows us to add more features to a class without modifying it

Here is an example of how to create a subclass:

    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
      def myMethod(self):
        print("Hello, my name is " + self.name)
    class Student(Person):
      def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade
      def myMethod(self):
        print("Hello, my name is " + self.name + " and I am in grade " + str(self.grade))
    myObject = Student("John", 36, 10)
    myObject.myMethod()

    Hello, my name is John and I am in grade 10


<a id="orga9fdce8"></a>

# Dictionaries

Dictionaries are used to store data values in `key:value` pairs. A dictionary is a collection which is ordered, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and have keys and values:

    myDict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
    }
    print(myDict)

    {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

We can access the items of a dictionary by referring to its key name, inside square brackets:

    x = myDict["model"]
    print(x)

    Mustang

Some important methods for dictionaries:

-   `.clear()` : removes all the elements from the dictionary
-   `.copy()` : returns a copy of the dictionary
-   `.fromkeys()` : returns a dictionary with the specified keys and values
-   `.get()` : returns the value of the specified key
-   `.items()` : returns a list containing a tuple for each key value pair
-   `.keys()` : returns a list containing the dictionary's keys
-   `.pop()` : removes the element with the specified key
-   `.popitem()` : removes the last inserted key-value pair
-   `.setdefault()` : returns the value of the specified key. If the key does not exist: insert the key, with the specified value
-   `.update()` : updates the dictionary with the specified key-value pairs
-   `.values()` : returns a list of all the values in the dictionary

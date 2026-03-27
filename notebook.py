"""
--> day 1
 ->python is a hight- level, interpreted, general-purpose programming language that is widely used for building applications, website, automations scripts, data analysis, artificial intelligence, and much more
 it was created by guido van rosuum in 1991
->python code runs line by line, so you don't need to compile it before running
->you don't need to declare variables types
->python runs on windows, linux, mac without changes because it is platform independent
->python can be typed dynamically // you don't need to declare variable types
->python is object oriented programming language
->python is large standard library // provides many built-in modules like("math, random, datetime")
->python is beginner-friendly 
->python is used in automation/scripting 
->syntax
  [import os 
 os.rename("file.txt","newfile.txt")]
->to check python is install or not we should use (python3 --version)

-->day2
->python character : in python, a character is not a separate data type like in some other languages (like c or java). instead, python treats a character as a string of length 1.
a character is simply a single letter,digit or symbol enclosed in quotes.
-> python syntax:
syntax means the rules of writing code in python
python syntax is very simple while compare to other languages
ex: print("hello world")

*in python indentation is very important 
python uses spaces to define blocks of code.

->output in python: output means displaying result on the screen.

-> comments in python : comments are used to explain code.
they can be represented in the form of (# : single line comment)(""" """ : multi line comment)

-->day 3
variables in python: A variable is name used to store data(value) in memory.
ex: x = 10
    name = "deepika"
    x stores number 10
    name stores text "deepika"

-> rules for naming variables
1. must start with a letter or _
2. cannot stat with a number
3. can contain letters, numbers, _
4. case-sensitive (age and Age are different) 

-> types of variables:
1. data types: python automatically decides the type.
2. dynamic typing: python allows changing the type of a variable
3. multiple assignment: you can assign multiple variables at once 
ex: a, b, c = 1, 2, 3
    print(a, b, c)
4. same value to multiple variables ex: z=y=x= 4
5. printing variables
6. type checking 
ex: x= 10
    print(type(x))

--> day 4
->python data types: a data type defines what kind of value a variable holds
ex: x = 10 // integer
name = "hi" // string
-> main data types in python : python has several built-in data types
1. numeric types: used to store numbers'
->types: 
..Int -> integer (whole numbers)
..Float -> decimal numbers
..Comples -> complex numbers
ex: a = 10 // int
    b = 3.12 //float
    c = 2 + 3j //complex

2. string (str): used to store text (characters)
ex: name = "deepika"

3. boolean(bool): represents (True or False)
ex: x = True
    y = False

4. list: used to store multiple values(mutable)(flexible collection)
ex: list = [1, 2, 3, "hi"]

5. tuple: same as list but immutable(cannot change)(fixed collection)
ex: tuple = (1, 2, 3, 4)

6. set: unorderded collection of unique values(mutable)(unique element)
ex: set = {1, 2, 3}

7. dictionary(dict): stores data in key- values pairs(mutable)(key-value mapping)
ex: student = { 
          "name" : "deepika",
          "age" : 23
          }

--> day 5
-> numbers in python : numbers are used to store numeric values in integers, decimals, etc
-> types numeric type
1. integer(int): whole numbers(no decimal point)
it can be positive or negative
no limit

2. float(float): numbers with decimal point
used for real numbers
precision may be approximate (due to computer representation)

3.complex(complex): numbers with real and imaginary parts
2 -> real part
3j -> imaginary part

--> day 6
->type checking in python : type checking means finding the data type of a variable
1.type() -> tells exact type
2. isinstance()-> checks type safely (checks if a variable belongs to a specific type.)

-> type casting(type conversion ): type casting means converting one data type into another
-> types of casting
1. implicit casting(automatic): python automatically converts types
2. expicit casting(manual): you convet types using functions (like int(), float(), bool(), str())

--> day6
-> string in python: a string is sequence of characters(letters, numbers, symbols).
-> it is written inside quotes:
1. single quotes ('')
2. double quotes ("")
3. triple quotes (''' ''' or """ """) used to write multi line command without initializing variable.

-> charcteristics of string 
1. orderd (each character has a position)
2. immuatble(cannot changed)
3. can store any characters

-> accessing characters(indexing): each character as an index
-> string methods:
1.case conversion method
.. upper() -> covert to uppercase
ex: s = "hello"
    print(s.upper())    
.. lower() -> convert to lowercase
ex: s= "hello"
    print(s.lower())
.. title()-> first letter capital
ex: s = "hello world"
    print(s.title()) // output : HELLO WORLD
..capitalize() -> first letter of string capital
ex: s = "python
    print(s.capitalize) // output : Python

2. checking methods(return True/False)
.. isalpha() -> only letters
ex: print("abc".isalpha())
.. isdigit() -> only numbers
ex: peint("123".isdigit())
.. isalnum() -> letters + numbers
ex: print("abs123".isalnum())
..isspace()-> only spaces
ex: print("  ".isspace())
.. islower()/isupper()
ex: print("abc".islower())
    print("ACD".isupper())

3.searching methods:
.. find() ->returns index(or -1)
ex: s = " python"
    print(s.find("t)) // output : 2
..index() -> returns index(error if not found)
ex: s = "python"
    print(s.index("o")) //output: 4
.. repacle &modify : replace()
ex: s = "hello world"
    print(s.replace("world", "python")) // output : hello python
.. splitting &joining : 
split() -> string - list
ex: s = "s,d,f"
    print(s.split(",")) // ['s', 'd', 'f']
join() -list -string
ex: l = ['a', 'v', 'd']
    print("-".join(l)) // a-v-d

6. removing spaces
..strip()-> removes spaces both sides
ex: s =" hello "
print(s.strip()) //hello
.. lstrip()/rstrip()
ex: print(s.lstrip()) //left space removed
    print(s.rstrip())// right space removed

7. counting &length
..count()
ex: s = "banana"
    print(s.count("a")) //output: 3
..len() -> (function, not method)
ex: print(len("hello")) //output:5

8.starts & ends
..startswith()
ex: s = "python"
    print(s.startswith("py")) output: True
.. endswith() 
ex: print(s.endswith("on"))

9.other useful methods
..swapcase() -> change case
ex: print("PyThOn".swapcase()) // output: pYtHoN
..zfill() -> add zeros
ex: print("5".zfill(4))//output: 00005

-->day7
->booleans: only True or False
used for decison making(conditions like : if, while)

-> operators : operators are used to perform operations on variables and values.
operators perform calculations and comparisions
types:
arithemetic
comparition
logoical
assignment
membership(like: in, not in)
identity: (like : is, is not)

--> day8
-> list : a list is a collection of items stored in ordered form.
..A built-in data type that stores set of values.
..it can store elemnets of different types(integers, float, string,etc)
..list is a mutable(can change)
..list allows duplicates
.. list is written in between square brackets[] and separated with kamma (,)
common list methods
1. append() -> used to add element
2. insert(index, value) -> userd to insert at specific position
3. remove(value) -> removes specific value
4. pop() -> removes last element
5. pop(index) -> removes specific elemnent
6. sort() -> sort list
7. reverse() -> reverse list
8. count(value) -> counts occurrences
9. index(value) -> find index
10. clear() -> removes all elemnts
11. copy() -> copy list

--day9
-> tuple: A built-in ata type that lets us create immutable sequence values
a tuple is similar to list but immutable
A tuple is ordered
tuples allow duplicates
tuple is written in paranthasis ()and also separated with kamma(,)

->common methods in tuple
.. count() ->used to count the value
.. index() ->used to find index value



"""
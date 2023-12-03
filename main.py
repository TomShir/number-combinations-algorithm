#What is Python?
'''Python is a high-level,dynamically-typed,interpreted,oop(object-oriented-programming) language created by Guido van Rossum in the year 1989 and was released to the public in 1991.The Python programming language was 
created at the National Netherlands Research Institute using the C programming language which was developed by Dennis Ritchie in 1972,shared a close interaction with hardware,was used to build operating systems and device 
driver and influenced many modern programming languages.Python is used in the fields of Data Science,Machine Learning,Web Development,back-end development,automation tasks,cybersecurity and robotics.The Python programming 
language has 35 reserved keywords and 68 built-in functions.Also,Python libraries are coded in C or Rust which are both low-level programming languages.'''
#What is a variable?
'''A variable is a symbolic name which references an object.Variables are stored in the RAM(Random Access Memory),where they have a name,content and an address.A Python interpreter would interprete all these 
attributes of a variable stored in memory.Variables can be mutable or immutable based on the type of object they are referencing.Variables are used to store different types of data for example:str,int,float,list,tuple,dict,set,
complex,None,bool,bytes,bytearray,range.In Python there are 3 types of variables,global,local and nonlocal.A global variable is a variable which is defined outside a function or inside a function using the global keyword.
These types of variables can be accessed and manipulated inside or outside functions.A local variable is a variable which is defined inside a function and belongs to the function's scope.These types of variables 
can never be used outside a function.If you attempt to use a local variable outside a function,you will get a NameError,saying that variable was'nt defined.A nonlocal variable is a variable  which is defined inside 
Python decorators(nested functions).In order to create a variable in Python,you first write the Python identifier followed by the equal sign and then the object the variable is referencing.'''
#What is a for loop?
'''A for loop is a method where the loop variable iterates over a subscriptable sequence,for example:str,list,tuple,set,dict,range.If you attempt to loop over a non-iterable sequence,you would get a TypeError,saying that 
object wasn't subscriptable.For loops print text vertically,repeat a block of code a specific amount of times,and have 2 loop control statements,break and continue.The break statement stops the execution of the for loop
immediately whereas the continue statement stops the current iteration of the for loop and skips it.These Python keywords are used inside if statements.'''
#What is an if statement?
'''An if statement is a conditional statement which checks if a particular condition has been met or not before the execution path.If statements are used for decision making in programming.If statements ultilise 
comparison operators,to compare 2 values,identity operators,to check if 2 objects are in the same memory location,membership operators,to check if a variable is present in a specific iterable container and logical 
operators,to add more functionality to if statements.If a condition was not met,an else or elif statement would be written handling that condition.'''
#What is a list?
'''A list is a data structure or collections data type,which stores multiple values,items or elements of a similar data type,in one variable.There are 2 types of lists,1 dimensional lists and 2 dimensional lists.
list functions:
list.append()-Adds an object to the end of the list. 
list.insert()-Takes 2 postional arguments,index,object.Appends an object to the list at  the specified index. 
list.reverse()-Reverses a list. 
list.sort()-Sorts a list in ascending order
list.count()-Counts the occurences of a value present in the list. 
list.index()-Returns the index of a  value present in the list. 
list.remove()-Removes an object from the list. 
list.clear()-Creates an empty list 
list.pop()-Deletes an object by the specified index.
del list[]-Deletes an object by the specified index.
list.extend()-Adds values existing from another iterable container to the end of the list. '''
#What is a Python identifier?
'''A Python identifier is a name for a variable,function,class or a Python module.In order to create  a Python identifier it must satisfy these conditions:
1. It cannot start with any numeric values
2. It cannot exceed 79 characters 
3.You cannot use Python keywords as Python identifiers 
4.You cannot use special characters except underscore characters in python identifiers. 
5.It must contain upper and lowercase letters. 
A Python identifier which starts with a underscore character is a private identifier.Whereas a Python identifier which starts and ends with 2 underscore symbols is a special language defined identifier'''
import time 
from colorama import Fore 
import sys 
from itertools import permutations 
import os
import pyttsx3
import timeit
pyttsx3.init()
try:
    integer=int(input('integer:'))
    strinteger=str(integer)
    combinations=list(permutations(strinteger))
    time.sleep(1)
    print(f'All  possible combinations of the given integer value:{strinteger}\n\t')
    time.sleep(1)
    for combination in combinations:
        print(f'{"".join(combination)}\n')
        time.sleep(1)
    else:
        timeit.timeit('''import time 
from colorama import Fore 
import sys 
from itertools import permutations 
import os
import pyttsx3
pyttsx3.init()
try:
    integer=int(input('integer:'))
    strinteger=str(integer)
    combinations=list(permutations(strinteger))
    time.sleep(1)
    print(f'All  possible combinations of the given integer value:{strinteger}\n\t')
    time.sleep(1)
    for combination in combinations:
        print(f'{"".join(combination)}\n')
        time.sleep(1)
    else:
        pass ''')
except ValueError:
    error_msg=f'ValueError:inappropiate value was entered'
    for text in error_msg:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{Fore.RED}{text}')
    else:
        print(f'{Fore.RESET}')
        time.sleep(1)
        os.system('cls')
        pyttsx3.speak("program exitted due to ValueError")
        sys.exit(f'{Fore.RESET}')
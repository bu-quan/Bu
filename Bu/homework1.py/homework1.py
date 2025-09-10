# File: homework1.py
#  --- Variables and Data Types ---
a = 10
print(a)
print(type(a))

b = 1.5
print(b)
print(type(b))

c = 3j
print(c)
print(type(c))

d = "hello"
print(d)
print(type(d))

e = [1, 2, 3]
print(e)
print(type(e))

f = {"name":  "Ellen", "favorite fruit":  "strawberry"}
print(f)
print(type(f))

g = (1, 2)
print(g)
print(type(g))

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))

i = True
print(i)
print(type(i))

j = None
print(j)
print(type(j))

k = [True, "blue", 12]
print(k)
print(type(k))

l = str(14)
print(l)
print(type(l))

m = 1e4
print(m)
print(type(m))

n = {"Richard", "Steven", "David"}
print(n)
print(type(n))
"""
1.I found 9 tyoes
2. They are int, float, complex, str, list, dict, tuple, bool, NoneType
3.e, h, and k are all lists, m and b and floats, l and d are strings
4. Because string(14) convert the int 14 to a string that represent 14.
5. n
"""

# Booleans
print(10 > 9)          # True, 10 is bigger than 9
print(10 == 9)         # False, 10 is not equal to 9
print(10 <= 9)         # False, 10 is not less than or equal to 9
print(bool("abc"))     # True, non-empty strings are true
print(bool(123))       # True, non-zero integers are true
print(bool(["apple", "cherry", "banana"]))  # True, non-empty lists are true
print(bool(True))      # True, the boolean True is true
print(bool(False))     # False, the boolean False is false
print(bool(0))         # False, zero is false
print(bool(""))        # False, empty string is false
print(bool(" "))       # True, non-empty string (even with just a space) is truthy
print(bool(()))        # False, empty tuple is false
print(bool([]))        # False, empty list is false
print(bool({}))        # False, empty dictionary is false
print(bool(True and False))  # False, AND of True and False is false
print(bool(True and True))   # True, AND of True and True is true
print(bool(False and False)) # False, AND of False and False is false
print(bool(True or False))   # True, OR of True and False is true
print(bool(True or True))    # True, OR of True and True is true
print(bool(False or False))  # False, OR of False and False is false
print(bool(not(False)))      # True, not False is true
print(bool(not(True)))       # False, not True is false
"""
1. The expression True represent sth. is not empty, nonzero, and True itself. Vice versa.
2. bool(" ") is True really surprised me because it provides no information in common sense.
3. bool(1) is True because int 1 is nonzero.
4. bool(12-3*4) is False because 12-3*4=0
"""

# Operators

# Arithmetic Operators
print(10 + 5)   # 15, + performs addition
print(10 - 5)   # 5, - performs subtraction
print(2 * 4)    # 8, * performs multiplication
print(6 / 3)    # 2.0, / performs division
print(5 % 2)    # 1, % returns the remainder
print(3 ** 2)   # 9, ** performs exponentiation 
print(15 // 2)  # 7, // performs division and rounding down

# Comparison Operators
print(5 == 2)   # False, == checks equality
print(10 != 10) # False, != checks inequality 
print(2 < 5)    # True, < checks less than 
print(12 > 5)   # True, > checks greater than
print(5 <= 6)   # True, <= checks less than or equal to
print(1 >= 10)  # False, >= checks greater than or equal to 

# Assignments Operators
x = 5
x += 5  # Equivalent to x = x + 5 and x becomes 10
x -= 4  # Equivalent to x = x - 4 and x becomes 6
x *= 3  # Equivalent to x = x * 3 and x becomes 18

# Logical Operators
"""
1. And returns True when the operands before and after are both True. Otherwise False. True and True. True and False
2. Or returns True when no less than one of the operands before and after are both True, otherwise False. True or False. False and False.
3. Not returns the negation of the operands. not False. not True
"""
"""
1. / returns a float and // returns an integer. // rounds down after /.
2. % returns the remainder of the devision.
3. I will use %. 4%3=1
4. x+=a means x=x+a, x-=1 means x=x-a, x*=a means x=x*a
"""

# Strings
my_string = "hello"
print(my_string)  # Prints: hello
print(my_string[0])  # Prints: h
print(my_string[1])  # Prints: e 
print(my_string[2])  # Prints: l 
print(my_string[3])  # Prints: l 
print(my_string[4])  # Prints: o 
print(my_string[-1])  # Prints: o 
print(my_string[1:3])  # Prints: el 
print(my_string[0:5:2])  # Prints: hlo 
print(len(my_string))  # Prints: 5 
print(my_string + "goodbye")  # Prints: hellogoodbye 
print(7 * my_string)  # Prints: hellohellohellohellohellohellohello 
"""
1. Slicing is subtract a smaller string with a start index and a end index. my_string[1:3] anb my_string[0:5:2]
2. Result: Hello, my name is Oski
3. Result: Hello, my name is Oski
4. The second one directly embed the variable name into the string
"""

# Terminal Commands

# cd: Navigates to a different folder. Example: cd Desktop
# ls: Lists files and directories in the current folder. Example: ls
# ls -a: Lists all files and directories, including hidden ones. Example: ls -a
# mkdir: Creates a new directory. Example: mkdir new_folder
# cat: Shows file contents. Example: cat file.txt
# pwd: Prints the current working directory path. Example: pwd
# cd ..: Moves to the parent directory. Example: cd ..
# cd .: Changes to the current directory. Example: cd .
# cd ~: Changes to the home directory. Example: cd ~
# cp: Copies files or directories. Example: cp 1.txt 2.txt
# mv: Moves or renames files or directories. Example: mv 1.txt 2.txt
# rm: Removes files or directories. Example: rm file.txt
# clear: Clears the terminal screen. Example: clear
# grep: Searches for patterns in files. Example: grep "pattern" file.txt

"""
1. touch 1.py, creates a new emtly file; nano 1.py, edits the file in the terminal; git status, check the status of the repository
2. ls -a shows the hidden files.
3. A hidden file is a file whose name begins with a dot.
4. ls -l, shows detailed information; rm -r directory, recursively removes directories and contents; cp -r dir1 dir2, recursively copies directories and contents. 
"""

# **PISCINE PYTHON**
_This project has been created as part of the 42 curriculum by \<bokim\>._

Welcome to the Python Piscine. 
The Piscine Python with total eleven modules will help you get to know basic and advanced concepts in python that you must know. 

Down below, I have explained useful concepts needed for each module, and I have also commented in detail inside the codes as well. 

Take a good look!
<br></br>

# Module Summary
- `module00`: 
- `module01`: 
- `module02`: 
- `module03`: 
- `module04`: 
- `module05`: 
- `module06`: 
- `module07`: 
- `module08`: 
- `module09`: 
- `module10`: 
<br></br>

# flake8
On Python projects, we will run **`flake8`** instead of `norminette`.

### Installation
- To install flake8, run the command below in your terminal.
```shell
python3 -m pip install flake8

# python<version> -m pip install flake8
```

### Using flake8
- To use flake8, run the command below in your terminal, inside the folder where your project files are.
```shell
python3 -m flake8

# python<version> -m flake8
```
- I highly recommand creating an alias for the use of flake8. My alias is as below:
```shell
alias fl='python3 -m flake8'
```

### Instruction for indentation
- To not get errors from flake8 due to indentation, follow the instructions below:
1. go to vscode settings
2. type "tab" in search bar
3. check if "**Editor: Tab Size**" is set to 4
4. click the "<u>Editor: Detect Indentation</u>" link in the description of "**Editor: Tab Size**"
5. Below "**Editor: Detect Indentation**", check the box for "**Editor: Insert Spaces**"

+) make sure to uncheck the box for "**Editor: Insert Spaces**" when your doing your C projects again for `norminette`
<br></br>

# Module00
## print()
In Python you can use `print()` to print things. 
```python
print("Hello World")
# output: Hello World

string1 = "Example"
print(string1)
# output: Example
```
You can also print something called an **f-string**.
- An f-string is a formatted string that starts with 'f' before the quote marks.
- To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
```python
name = bokim
school = 42

print(f"Hello my name is {name} and I am from school {school})
# output: Hello my name is bokim and I am from school 42
```
## input()
In Python you can use `input()` to take in user input.
- User inputes are received as strings.
```python
name = input("Enter your name: ") # gets user input and stores it in variable "name"
print(f"Hello {name}!") 
#output: Hello (user_input!)
```
## int()
In Python you can change a type of variable into an integer using `int()`.
```python
age = int(input("Enter your age: "))
# age must be changed into an integer using int() because input() is recieved as a string

print(f"You are {age} years old!")
#output: You are (user_input) years old!
```
## User Defined Functions
In Python, you can create your own functions by using the keyword `def`.
```python
def my_function() -> None: # a function that takes no parameters and returns nothing
    print("This is my function!")

my_function()
#output: This is my function!
```
## range()
In Python, you can use `range()` to generate a sequence of numbers.
- It is most commonly used in `for` loops to repeat an action a specific number of times without having to manually type out a list.
```python
for i in range(1, 10)
    print(i)
#output: 1 2 3 4 5 6 7 8 9 10 (newline after each number)
```
<br></br>
# Module01
## Object Oriented Programming

## docstrings

## class

## Inheritance

## if __name__ == __"main"__

## class functions

## static method / class method

# Module02
## open() / close()
## try / except / finally
## User defined errors
## raise

# Module03
## sys
## sys.argv
## len() / sum() / max() / min()
## math
## tuple
## split()
## set() / union() / intersection() / difference()
## dict() / keys() / values() / items()
## get() / update()
## next() / iter() / range()
## sorted()

# Module04
## read()
## write()
## sys.stdin / sys.stdout / sys.stderr

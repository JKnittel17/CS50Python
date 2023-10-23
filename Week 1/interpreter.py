"""
Prompt:
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point 
value formatted to one decimal place. Assume that the users input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
"""

# Ask user for input --- split input by " " and store into unique variables
x, y, z = input("Expresion: ").split(" ")

# Change x and z to float
x = float(x)
z = float(z)

# Evaluate and Print Expression --- the problem page showed that 1.3 was the solution to 4 / 3, so I have inferred rounding is needed
match y:
    case "+":
        print(round(x + z, 1))
    case "-":
        print(round(x - z, 1))
    case "*":
        print(round(x * z, 1))
    case "/":
        print(round(x / z, 1))


    
"""
Alternate Solution 1) In our match cases, we could have stored the evaluated expression into a variable, and then at the end of the code had a print statement for the result.

match y:
    case "+":
        result = x + y
    case "-":
        result = x - y
    case "*":
        result = x * y
    case "/":
        result = x / y

print(round(result, 1))


Alternate Solution 2) Instead of "round" function, you could use printf statements with :1f , i personally just think round is more readable to the naked eye

"""
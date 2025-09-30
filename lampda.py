#  lampda function

#  A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

#  The syntax of a lambda function is as follows:
# lambda arguments: expression
# The expression is evaluated and returned when the function is called.
# Here is an example of a lambda function that adds two numbers:
add = lambda x,y: x+y;
print(f"the sum of two number is : {add(4,6)}");
# Here is an example of a lambda function that multiplies two numbers:
multiply = lambda x,y: x*y;
print(f"the multiplication of two number is : {multiply(4,6)}");
# Here is an example of a lambda function that finds the maximum of two numbers:
maximun = lambda x,y: x if x>y else y; #explanation x if x>y else y means if x is greater than y return x otherwise return y 
print(f"the maximum of two number is : {maximun(7,9)}")
# Here is an example of a lambda function that finds the minimum of two numbers:
minimum = lambda x,y: x if x< y else y;
print(f"the minimum of two number is : {minimum(99,45)}");
# Here is an example of a lambda function that squares a number:
square = lambda x: x**2;
print(f"the square of x is : {square(4)}");
# Here is an example of a lambda function that cubes a number:
cube = lambda x : x**3;
print(f"the cube of x is : {cube(3)}");
# Here is an example of a lambda function that checks if a number is even or odd:
is_even = lambda x: True if x%2 == 0 else False;
print(f"the number is even : {is_even(7)}");
is_odd = lambda x: True if x%2 != 0 else False;
print(f"the number is odd : {is_odd(3)}");

# here is an example of a lampda function that squares all the numbers in a list using map function
numbers = [1,2,3,4,5,6,7,8,9,10];

squared_numbers = list(map(lambda x: x**2, numbers));
print(f"the suared numbers in the list is : {squared_numbers}");
# here is an example of a lampda function that filters all the even numbers in a list using filter function
even_numbers = list(filter(lambda x: x%2 == 0,numbers))
print(f"the even numbers is the list is : {even_numbers}")

odd_numbers = list(filter(lambda x: x%2 != 0 , numbers));
print(f"the odd numbers in the list is : {odd_numbers}");

# here is an example of discount calculation using lampda function
prices = [100,200,300,400,500];
discounted_prices = list(map(lambda x: (x-x*0.1),prices));
print(f"the discounted prices is : {discounted_prices}");

# practice problems
# 1. write a function thar takes two numbers as input and returns their product using a lambda function.

# 2. write a function with default parameter welcome(name="Guest") that prints a welcome message using a lambda function.

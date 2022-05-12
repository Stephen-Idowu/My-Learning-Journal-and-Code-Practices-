Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> # The below program allows users to enter thier name with a welcome message
>>> greeting = ('Hello')
>>> name = input('Enter your name')
Enter your name Stephen 
>>> print(greeting + name)
Hello Stephen 


>>> # A simple program that help employees to know how much thier paycheck is
>>> Hour = 40
>>> Rate = 3.5
>>> print(Hour * Rate)
140.0


>>> # A simple operation to determine
>>> # 1. width//2
>>> # 2. width/2.0
>>> # 3. height/3
>>> # 1 + 2 * 5
>>> # if width = 17, height = 12.0
>>> 
>>> # Solution
>>> width = 17
>>> height = 12.0
>>> 
>>> print(width//2)
8
>>> print(width/2.0)
8.5
>>> print(height/3)
4.0
>>> print(1 + 2 * 5)
11
>>> 
>>> # Boolean Expression
>>> 
>>> # This type of expression are either True or False
>>> 
>>> # The operator == is used to tell if two operands are True, if they are equal and False if otherwise.
>>> 
>>> # An Example
 
>>> 5==5
True
>>> 5==6
False
>>> 
>>> # True and False are special value. They belong to the class bool. They are not string.
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>


>>> # The boolean expresion uses the following comparison operators.

>>> # x is not equal to y, x ! = y
>>> # x is greater than y, x > y

>>> # x is less than y,   x < y
>>> # x is greater than or equal to y,  x >= y
>>> # x is less than or equal to y,  x <= y
>>> 
>>> # x is the same as y,  x is y
>>> # x is not the same as y,  x is not y
>>> 
>>> 
>>> # Note '=' is an assignment operator, while '==' is a comparison operator.

>>> # Another set of operators in  python are Logical Operator. They include: and, or, and not. The meaning of these operator are similar to their meaning in English.
>>> 
>>> # An Example
>>> 
>>> # x > 1 and x < 7. Can only be true if x is greater than 1 and less than 10.
>>> # Also, a%2 == 0 or a%3 == 0, can only be true if either of the condition is true, that is, if the number is divisible by 2 or 3.

>>> # Lastly, the not operator negates a boolen expression. so not (a > b) is true if a > b is false; that is, if a is less than or equal to b.

>>> # Condtional Execution 
>>> # Changing the conditions and behavior of our program is a task we cannot shy away from. This can be achieved through conditional statement.
>>> 
>>> # Examples of Conditional Statement.
>>> #1. if statement
>>> 
>>> if x > 0:
	print('x is positive')
>>> # The boolean expression which follows the if statement is called the condition.
>>> # The if statement always end with a colon character (:) and the lines(s) after the if statement are indented.





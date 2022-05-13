Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Day 2
>>> 
>>> # It's good to note that when writing an if condtional statement.
>>> # If the logical is true, the indented statement gets executed. But if the logical statement is false, the indented statement is skipped.
>>> 
>>> x = 5
>>> if x < 7:
	print('Small')

	
Small

>>> # 2. Another form of the if statement is the alternative execution.
>>> # This type of execution has two possibilities and the conditions determines which one gets executed.
>>> 
>>> # An example

>>> x = 4
>>> if x % 2 == 0:
	print('x is even')
else :
	print('x is odd')

	
x is even
>>> # The returned result is zero because there was no remainder.


>>> #3. The Chained conditionals helps us to compute programs that has more than two possibilities.
>>> # An example of such statement can be in this format
>>> 
>>> # if x < y :

>>> #  if x < y;
>>> #      print('x is less than y')
>>> #  elif x >y:
>>> #	   print('x is greater than y')
>>> #  else:
>>> #	   print('x and y are equal')


>>> # elif is an abbrevation of "else if". There can be many elif statement.
>>> # But if there is an else clause it has to be at the end.
>>> 
>>> # 4. Nested Contionals. There are times when we want to write a program that evaluates more than two coindtions with different metrics.
>>> 
>>> # An example of such  code could be in this format.
>>> 
>>> x = 7
>>> y = 7
>>> if x == y:
	print('x and y are equal')
else:
	if x < y :
		print(' is less than y')
	else :
		print('x is greater than y')

		
x and y are equal

>>> # From the example above the outer conditional contains two branches.
>>> # The first branch contains a simple statement.
>>> # While the second branch contains another if statement,
>>> # which has two branches of its own.
>>> 
>>> # Try and Except.
>>> # There are times its possible we write a progrsm and expected and unexpected might occur
>>> # Python has inbuilt funtion to elp us controlld this.
>>> 
>>> # The idea of try and except is to help execute some statement if there is an error with a program as a result of the instruction.
>>> 
>>> 
>>> inp = input('Enter Fahrenheit Temperature:')
Enter Fahrenheit Temperature:
>>> try:
	fahr = float(inp)
	cel = (fahr - 32.0)* 5.0 / 9.0
	print(cel)
except :
	print('Please enter a number')

Please enter a number


>>> # Short-circuit evaluation of logical expression
>>> 
>>> # Python has the capacity to determine what would be the end result of a logical expression as a result of some certian condition.
>>> # When the evaluation of a logical expression stops because the overall value is known, it is called short-circuiting the evaluation.
>>> 
>>> # For example

>>> x = 8
>>> y = 4
>>> x >= 2 and (x/y) > 2

False

>>> x = 2
>>> y = 1
>>> x >= 2 and (x/y) > 2

False

>>> x =  1
>>> y = 0
>>> x >= 2 and (x/y) > 2

False

>>> # The short circuit behavior of python can lead to technique called the guardian pattern.
>>> 
>>> # Examples include:

>>> x  = 1
>>> y = 0
>>> x >= 2 and y != 0 and (x/y) > 2

False


>>> x  = 2
>>> y = 1
>>> x >= 2 and y != 1 and (x/y) > 2

False


Title: Calculating Secret Member IDs
A small club wants to give each member a 4-digit ID number with a 5th "secret number" at the end to make sure nobody typed the ID wrong.

Write a Python file called secret_id.py that starts with a 4-digit ID split into separate variables:

Python
id_1 = 4
id_2 = 2
id_3 = 8
id_4 = 5

Write a program to find the secret check number using these steps:

Create a function called fix_number(num). If num is bigger than 9, it should return num - 9. Otherwise, it should return num.

Multiply id_2 and id_4 by 2, and run both through your fix_number function.

Keep id_1 and id_3 as they are.

Add all 4 numbers together to get a total.

Find the check number using this math formula: (10 - (total % 10)) % 10.

Print out the full 5-digit ID as one single string (for example, if the ID is 4285 and the check number is 8, print "42858").





2. Explanation of Assessment Goals

This problem checks if the person knows how to write functions, run math operations on variables, and put text together in Python. It directly tests concepts learned in the first two weeks of class, like order of code execution, converting numbers to text with str(), and using modular arithmetic (%).

The trickiest part for a beginner will be making sure the function is defined near the top of the file before calling it, and converting all the numbers into strings before combining them. Learning this helps students avoid silly Errors.

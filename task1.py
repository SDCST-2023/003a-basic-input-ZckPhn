#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

example:
What is your name:Dwayne Johnson
What ir your email:rock@aol.com

Your name is Dwayne Johnson, and your email is rock@aol.com

What is your name:Jackie Chan
What ir your email:crazyAsian@qq.com

Your name is Jackie Chan, and your email is crazyAsian@qq.com

"""
question = "What is your name?"
response = input(question) 

question = "What is your email address?"
response = input(question)

print(f"My name is Rumple Stiltkin,{response}")
print(f"My email address is Farqua@gmail.com,{response}")
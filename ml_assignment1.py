# -*- coding: utf-8 -*-
"""ML-ASSIGNMENT1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12r0gaMuDTVjciUmofmOavavcGdThHFYF

#WAP to accept two numbers from the user and display their sum
"""

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = a+b
print("The sum of two numbers are: ",c)

"""#WAP to accept radius of a Circle from the user and calculate area and circumference"""

r = float(input("Enter your radius: "))
area = 3.142*r*r
circum = 2*3.142*r
print("The area of circle is {} and circumferemce is {} ".format(area,circum))

"""WAP to accept roll number , grade and percentage as input from the user and display it back"""

roll = int(input("Enter your roll number: "))
grade = input("Enter your grade of your exams: ")
per = input("Enter your percentage of your exams: ")
print("Your roll no. is {}, Your grade that you scored in your exams is {} and your percentage is {} ".format(roll,grade,per))

"""Write a program that asks the user to enter his/her name and age. Print out a message , displaying the user’s name along with the year in which they will turn 100 years old"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
c = 100-age
d = 2022+c
print("{} will turn 100 at the age of {} and the year will be {} ".format(name,c,d))

"""Write a program that asks the user to input 2 integers and adds them . Accept both the numbers in a single line only"""

print("Enter two numbers: ")
a,b = map(int,input().split())
c = a+b
print("Addition of two numbers is: ",c)

"""Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them."""

name = input("Enter your first name and last name: ")
li = []
for i in name:
  li.append(i)
li.reverse()
print(li)
for i in li:
  print(i)

"""#WAP to accept an integer from the user and check whether it is an even or odd """

num = int(input("Enter your number: "))
if num%2==0:
  print("Even number")
else:
  print("Odd number")

"""#WAP to accept a character from the user and check whether it is a capital letter or small letter. Assume user will input only alphabets"""

n = input("Enter your character: ")
if n>'A' and n<'Z':
  print("Capital letter")
elif n>'a' or n<'z':
  print("Small letter")
else:
  print("Enter in specified format")

"""#WAP to accept a character from the user and check whether it is a capital letter or small letter or a digit or some special symbol"""

n = input("Enter your character: ")
if n>'A' and n<'Z':
  print("Capital letter")
elif n>'a' and n<'z':
  print("Small letter")
elif n>'0' and n<'9':
  print("Digits")
else:
  print("It is some special symbol")

"""WAP to accept 3 integers from the user and without using any logical operator and cascading of relational operators , find out the greatest number amongst them"""

def maximum(a, b, c):
  
    if (a >= b) and (a >= c):
        greatest = a
  
    elif (b >= a) and (b >= c):
        greatest = b
    else:
        greatest = c
          
    return greatest
maximum(2,7,5)


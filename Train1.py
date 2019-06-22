# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:00:33 2019

@author: rohit
"""

def add(a,b):
    try:
        return a + b
    except Exception as a:
        print('The additiob raises an Error ',a)
 
def sub(a,b):
    try:
        return a - b
    except Exception as s:
        print ("The Subtraction raises an Error",s)
  
  
def div(a,b):
    try:
        return a / b
    except Exception as e:
        print('The division raises an Error ',e)
    


def multiply(a,b):
    try:
        return a * b
    except Exception as m:
        print('The Multiplication raises an Error ',m)
try:
    print('Mini Calculator in Python')
    print("1.> Addition")
    print("2.> Subtraction")
    print("3.> Division")
    print("4.> Multiplication")
    print("5. Exit")
    choice = input("Please Enter your choice(1/2/3/4):")
    if choice >= "1" and choice <= "4":
        a = int(input("Please Enter 1st Number choice = %d :"%choice))
        b = int(input("Please Enter 2nd Number choice = %d:"))
        if choice == "1":
            print(a,"+",b,"=", add(a,b))
        elif choice == "2":
            print(a,"-",b,"=", sub(a,b))
        elif choice == "3":
            print(a,"/",b,"=", div(a,b))
        elif choice == "4":
            print(a,"*",b,"=", multiply(a,b))
        elif choice == "5":
            exit()
        else:
            print ("Please Enter a Valid Input 1 2 3 4")
except Exception as c:
    print ("The Error is thrown",c)
finally:
       print("done!")            
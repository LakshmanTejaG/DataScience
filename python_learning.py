#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 15:18:27 2019

@author: lakshmanteja
"""
# User input
name = input("Please enter your name:")
age = input("Please enter your age:")

print("your name is:{} and your age is: {}".format(name, age))

import sys
import argparse

parser = argparse.ArgumentParser(description="Input parsing")
parser.add_argument('-v', '--version',action='version',version='%(prog)s v1.0')

required = parser.add_argument_group('required arguments')
required.add_argument('-n','--name', help='Enter your name')
required.add_argument('-a','--age', help='Enter your age')
required.add_argument('-e','--education', help='Enter your eduction')

args = parser.parse_args(args=None if sys.argv[1:] else ['-h'])


print('Your name:{} - your age: {} - your education:{}'.format(args.name,args.age,args.education))



#python control statements
# if
a=40
b=50
if a < b :
    print ("A is less than B")
    
# if and elif  
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print('a is less than b')
  
# whileloop     
attandance = input('How many days a school for week:')
student =int(attandance)
mark = 0
while student > 6:
    student = student-1
    mark = mark +1
    print('Going school',mark)
print('Full attandance')

# forloop
fruits_list = ['apple','mango','orange','banana','grap','cherry']
order_list=0
for fruits in fruits_list:
    order_list = order_list+1
    print('order number{} is for {}'.format(order_list,fruits))
  
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)
  
#Exit the loop when fruits is "banana with continuous":
fruits_list = ['apple','mango','orange','banana','grap','cherry']
order_list=0
for fruits in fruits_list:
    if fruits == 'orange':
        continue
    order_list = order_list+1
    print('order number{} is for {}'.format(order_list,fruits))

#Exit the loop when fruits is "banana with continuous":
fruits_list = ['apple','mango','orange','banana','grap','cherry']
order_list=0
for fruits in fruits_list:
    if fruits == 'orange':
        break
    order_list = order_list+1
    print('order number{} is for {}'.format(order_list,fruits))

############################
## Nested loops in python ##
############################
    
# Whileloop to print prime number
user_input=input('Enter your number:')
input_number=int(user_input)
prime_divisor=2
primer_number=True
while prime_divisor < input_number:
    if input_number%prime_divisor==0:
        primer_number=False
        break
    prime_divisor = prime_divisor +1
if primer_number:
    print(input_number,'is prime number')
else:
    print(input_number,'is not prime number')
print('Good Job')


# Nested loop: while in while
start_number=100
end_number=200
while start_number <= end_number:
    prime_divisor=2
    assume_primer_number=True
    while prime_divisor < start_number:
        if start_number%prime_divisor==0:
            assume_primer_number=False
            break
        prime_divisor=prime_divisor+1
    if assume_primer_number:
        print(start_number,'is prime number')
    start_number=start_number+1
print('all done')


# Nested loop: while in for
start_num=2
end_num=100
current_num=start_num
for current_num in range(start_num,end_num+1):
    divisor=2
    prime_assume=True
    while divisor < current_num:
        if current_num%divisor==0:
            prime_assume=False
            break
        divisor=divisor+1
    if prime_assume:
        print(current_num,'Is Prime Number')
print('Primer Numbers Printed')

#Nested loop: for in for
start_num=2
end_num=200


#Function
 
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

import re

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)




import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument('-i','--input', help='Please provide a file name')

parser.add_argument('-t','--text', help='Please enter text to store in file')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    
f = open(args.input , 'w')
f.write(args.text)

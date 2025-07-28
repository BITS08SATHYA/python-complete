import math
from readline import insert_text

# print('Hello python!')

# Identify Classtypes
x = "vino"
# print(x.__class__.__name__)
# print(type(x))

# variables
my_var = 10
# print(my_var)

# java
# Static vs Dynamic programming
# x1 = 4
# x = "sathya";
# str = 'hello'
# print(type(str))
str1 = '''
    hello 
    how are you
'''
# print(str1)

# reserve keywords
# for = 5

# Integer
# print(type(10))

# d1 = None
# print(type(d1))
#
# d2 = 5 > 2
# print(d2)

# Arithmetic
# + , - , *, / , //, %, **

x = 2
y = 4
# print(x ** y)

# Floor and Ceiling
val = 10.25
# print(math.floor(val))
# print(math.ceil(val))

# Relation vs Comparison operators
# <, > , <=, >=, is not
# x = 4
# if (x == 5):
#     print(True)
# else:
#     print(False)

# use Ord operator for getting ascii values of characters
cx = 'a'
cy = 'b'
# print(ord(cx) == ord(cy))
# print(cx != cy)
# print( 10 < 20 != 30 < 40)
# print( 10 != 20 != 30 != 40)

# Logical operators
# And (&&) , or (||) , not (!)

t1 = 5
t2 = 0

# print(not t2)

# Reading a input
# r1 = input('Enter a number: ')
# print("You entered: " , r1)

str2 = '5'
# print('hello' + str2)

# def add(a,b):
#     return a + b
#
# add(5, 2) # callable

# if-else statements
x = 4
y = 2
# if (x > y):
#     print(True)
# else:
#     print(False)
#
# for g in range(1,10,2):
#     print(g)

n  = 10
i = 0
# while i < n:
#     print(i)
#     i = i + 1

# list = [1,2,3,4,5]
#
# for i in list:
#     if i % 2 == 0:
#         print(str(i) + ' - continue')
#         continue
#     print(i)

# list
'''
insert(index, value)
append(value)
extend([elements or list of elements])
del list[index]
list[start:end]
'''

l1 = [1,2,3, 2.85]
print(len(l1))
l2 =  [56.2, 'python'] + l1
l2.insert(1, 20)
l2.append(100)
l2.extend([300, 'vino'])
del l2[1]
# print(l2[0:3])

# string
my_str = 'Hello python'
my_str2 = '10,20,30,40,50'
print(my_str2.split(','))




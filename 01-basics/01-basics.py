# from math import pi, pow
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
remove(element)
pop(index)
clear()
count(x)
list.sort(reverse=True or False)
list.copy()  # mutable copy
'''

# l1 = [1,1,2,3, 2.85]
# print(len(l1))
# l2 =  [56.2, 'python'] + l1
# l2.insert(1, 20)
# l2.append(100)
# l2.extend([300, 'vino'])
# #l2.remove(56.2) # element
# # del l2[1]  # index
# print(l2)
# l2.pop(0)
# print(l2)
# print(l1.count(2))
# l1.sort(reverse=False)
# print(l1)
# copy_list = l1.copy()
# copy_list.insert(0,101)
# print(copy_list)


# string
# my_str = 'Hello python'
# my_str2 = '10,20,30,40,50'
# print(my_str2.split(','))

# Tuples
llist = [1,2,3,4,5]  # mutable
# print(llist)
# llist[0] = 100
# print(llist)

'''
    len(tp)
    sum(tp)
    max(tp)
    min(tp)
    5 in tp
'''

tp = (1,2,'Hello',2.4,5)  # immutable
# tp =  tp[0:] + (101,)
# print(tp)
# del tp
# print(tp)


l1 = [10, 54, 2, 61, 15]
l2 = [2, 61, 15]

# for x in l1:
#     if x in l2:
#         print('Common lements', x)
common = set(l1) & set(l2)
Ncommon = set(l1).symmetric_difference(l2)

# print(Ncommon)

# Dictionary
D = {
    'USA': 100,
    'INDIA': (50, 'Sathya'),
    'UK': [200, 'London']
}

# print(D['UK'])

# print(D.keys())

# print(len(D))

# print('UK' in D)
D['Aus'] = [1,2,3,4,5]

# print(D)

# del D['USA']

# for i in D.keys():
#     print(i,D[i])

def myadd(*a):
    sum = 0
    for i in a:
        sum += i
    return sum
#
# res = myadd(1,15,1,1,1)
# print(res)

print(dir(math))

# for x in dir(math):
#     print(x)

print(pi)
print(round(pow(2,4)))






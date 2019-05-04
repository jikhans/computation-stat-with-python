# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:21:55 2019

@author: Jikhan Jeong
"""

## 2019_05_03_Computational Statistics_intro_python
## reference: https://people.duke.edu/~ccc14/sta-663/IntroductionToPythonSolutions.html

import os
print("Current Working Directory " , os.getcwd())
os.chdir("C:/python/a_python/2019_sl/")

for i in range(1,10):
    print(i)

i = 1
while i<10:
        print(i)
        i+=1
        
def divisor(a,b):
    print(a/b)

divisor(10,2)    

# try and except

a ="1"

type(a) # str_____________

try:
    b =a +2
except:
    print(a, " is not a number")
    

a1 =1
type(a1) # int____________
   
try:
    b1 =a1 +2
except:
    print(a, " is not a number")
    
##
def divisors(a,b):
    try:
        print(a/b)
    except:
        if b==0:
            print("denominaor is zero")
        else:
            print(float(a)/float(b))

divisors(2,"2") #1.0
divisors(2,0)


# String_______________________________________________________________________

a = "A string of characters, with newline \n CAPITALS, etc." # \n block change
print(a)
b=5.0
new = a+ "\n We can formating %.2f"
print(new %b)


a = "ABC DEFG"
print(a[1:3])
print(a[0:5])

a = "ABC defg"
print(a.lower())
print(a.upper())
print(a.find('d'))
print(a.replace('de','a'))
print(a)
b = a.replace('def','aaa')
print(b)
b = b.replace('a','c')
print(b)
b.count('c')

# List, Tuples, Dictionaries___________________________________________________


# List []______________________________________________________________________

a_list = [1,2,3,"this is a string",5.3]
b_list = ["A","B","F","G","d","x","c",a_list,3]

print(b_list[7:9])

a = [1,2,3,4,5,6,7]
a.insert(0,0)
print(a)
a.append(8)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop()
print(a)
a.remove(3)
print(a)
a.remove(a[4])
print(a)

even =[x for x in range(10) if x % 2 == 0] # a%b = remain of a/b
even

first =  "It was a dark and stormy night."
charaters = [x for x in first]
print(charaters)

def sqr(x): return x **2
c=list()
a = [2,3,4]
b = [10,5,3]
c = map(sqr,a) # map(aFunction, aSequence)
print(c)

d=map(pow,a,b)
print(d)

# tuple ()_____________________________________________________________________

a =(1,2,3,4)
print(a)
a[1]

a = (1,"string in a tuple",5.3)
b = (a,1,2,3)

print(a)
print(b)

my_pets = ("Chestnut", "Tibbs", "Dash", "Bast")
(aussie,b_collie,indoor_cat,outdoor_cat) = my_pets
print(aussie)
cats=(indoor_cat,outdoor_cat)
print(cats)

# Dictionaries_________________________________________________________________

a = ["A","B","C","D"] #list example
print(a)

a = {'anItem': "A", 'anotherItem': "B",'athirdItem':"C",'afourthItem':"D"} # dictionary example
print(a[1])
print(a['anItem'])
print(a)

# The dictionary does not order the items, and you cannot access them assuming 
# an order (as an index does). You access elements using the keys.

# Set__________________________________________________________________________

from sets import Set
fruits = Set(["apples","oranges","grapes","bananas"])
citrus = Set(["lemons","oranges","limes","grapefruits","clementines"])

citrus_in_fruits = fruits & citrus   #intersection
print(citrus_in_fruits)

diff_fruits = fruits - citrus        # set difference
print(diff_fruits)

diff_fruits_reverse = citrus - fruits  # set difference
print(diff_fruits_reverse)

citrus_or_fruits = citrus | fruits     # set union | or
print(citrus_or_fruits)



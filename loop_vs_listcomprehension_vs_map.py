# python loop
# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''' 
def example(): 
    mylist = [] 
    for x in range(100): 
        mylist.append(sqrt(x)) 
'''

# timeit statement
t = timeit.timeit(setup=mysetup,
                  stmt=mycode,
                  number=10000)
print(f"Using for loop time required = {t}")

# Using list comprehension
mycode = ''' 
mylist = [sqrt(i) for i in range(100)]
'''
t = timeit.timeit(setup=mysetup,
                  stmt=mycode,
                  number=10000)
print(f"Using list comprehension time required = {t}")

# Without lambda list comprehension
mycode = ''' 
mylist = [i*i for i in range(100)]
'''
t = timeit.timeit(setup=mysetup,
                  stmt=mycode,
                  number=10000)
print(f"Without lambda Using list comprehension time required = {t}")
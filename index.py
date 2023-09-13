hjhj
# whitespae is important
listOfNumbers = [1,2,3,4,5,6];

for number in listOfNumbers:
    if(number % 2 == 0):
        print(number," is even")
    else:
        print(number," is odd")

print("All done")

# importing module
import numpy as np

A = np.random.normal(25.0,5.0,10)
print(A)

# Lists
x = [1,2,3,4,5,6]
print(len(x))
print(x[:3])
print(x[3:])
print(x[-2:])
x.extend([7,8])
print(x)
x.append(9)
print(x)

y = [10,11,12]
listOfLists = [x,y]
print(listOfLists)
print(y[1])

z=[3,4,2,5,1]
z.sort()
print(z)
z.sort(reverse=True)
print(z)


# Tuples(these are just immutable lists)
x = (1,2,3)
print(len(x))
# x[1] = 5   #will not work since immutable
print(x)
x = ('hi', 11, 45.7)
print(x)
x = (55, (6, 'hi'), 67)
print(x)

y = (4,5,6)
print(y[2])

listOfTuples = [x,y]
print(listOfTuples)

(age,income) = "32,1200000".split(',')
print(age)
print(income)


# Dictionaries(like a map or hash in javascript)
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep space nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print(captains["Voyager"])
print(captains.get("Enterprise"))
print(captains.get("sfdssd"))

for ship in captains:
    print(ship + ": " + captains[ship])


thisdict = dict(name = "John", age = 36, country = "Norway")   #with dict constructor
print(thisdict) 

# Functions
def SquarIt(x):
    return x * x
print(SquarIt(2))    

def DoSomething(f, x):     #passing function around as parameter
    return f(x)

print(DoSomething(SquarIt,3))    

print(DoSomething(lambda x:x * x * x,3))   #lambda function let you incline simple functions 





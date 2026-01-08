# Reduce Function is a in-build Function which reduce the sequence to a single value
from functools import reduce
def addTwo(x,y):
    return x+y
def secondTopper(a,b):
    if a>b:
        return a
    else:
        return b
    
test_marks = [50,65,70,85,99]
sum = (reduce(addTwo,test_marks))
print(sum)
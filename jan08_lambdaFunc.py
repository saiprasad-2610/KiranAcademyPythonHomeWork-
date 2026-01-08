from functools import reduce

# map using lambda function
test_marks = [50,82,95,77,65]
res = list(map(lambda a: a+5, test_marks))
print(res)

# filter using lambda function
test_marks1 = [50,82,95,77,65]
topper = list(filter(lambda a:a>60,test_marks1))
print(topper)

# Reduce using lambda Function
test_marks2 = [50,60,85,95,86]
max_value = reduce(lambda a,b: a if a>b else b,test_marks2)
print(max_value)


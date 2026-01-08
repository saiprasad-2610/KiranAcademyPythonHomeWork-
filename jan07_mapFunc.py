test_marks = [67,80,66,59,95]
grace_marks =[]

# # .............1................
# for i in test_marks:
#     grace_marks.append(i+5)
# print(grace_marks)

# # ..............2...............
# def addFive(n1):
#     return n1+5
# for i in test_marks:
#     grace_marks.append(addFive(i))
# print(grace_marks)  

# ...............By Using Map function........... 
# =====> map(function,sequence)

def addFive(n1):
    return n1+5
grace_marks=list(map(addFive,test_marks))
print(grace_marks)
# # Decorators: this are higher Order function
#             # without changing tje original function we can modify/enhance feature of original function with help of Decorators
    
    
# def myDecorator(fun):
#     def innerDecorator():
#         print("****************")
#         fun()
#         print("****************")
#     return innerDecorator


# @myDecorator
# def myProfile():
#     print("Hello Sai")


# # res = myDecorator(myProfile)
# myProfile()




def threeAdd(fun):
    def inner(a,b,c=0):
        return fun(a,b)+c
    return inner

@threeAdd
def addtwo(a,b):
    return a+b
print(addtwo(2,5,3))
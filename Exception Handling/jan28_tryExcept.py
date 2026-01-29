# try
# except
# else
# finally
# raise

# try:
#     x = int(input("Enter 1st Number: "))
#     y = int(input("Enter 2nd Number: "))
#     print(x/y)
# except ValueError as e:
#     print("Error.... Input must be integer")
# except ZeroDivisionError as e:
#     print("infinity..")
# else : 
#     print("Successfully done..")
# finally:
#     print("This is Division completed..")
    
class customException(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(msg)
marks = 50
if marks<60:
    obj = customException("error")
    raise obj



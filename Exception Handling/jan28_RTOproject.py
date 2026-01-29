class AgeTooLowException(Exception):
    def __init__(self, msg):
        self.msg = msg
class AgeTooHighException(Exception):
    def __init__(self, msg):
        self.msg = msg
try:
    age = int(input("Enter the Age: "))
    if age <18:
        obj1 = AgeTooLowException("Not Eligible as age is low")
        raise obj1
    elif age>75:
        obj2 = AgeTooHighException("Not Eligible as Age is More")
        raise obj2
    else:
        print("Hey.. Welcome To Pune-RTO..\n You can Apply for license ")
except ValueError as e:
    print("Age must be Integer..")
except AgeTooLowException as e:
    print("Error, Age is low...")
    print(e)

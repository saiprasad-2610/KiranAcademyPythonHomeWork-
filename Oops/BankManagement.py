class Bank:
    def __init__(self,n,acc,pas,amo):
        self.__name = n
        self.__account_number = acc
        self.__pas = pas
        self.__amo = amo
    
    def __str__(self):
        return f"Name: {self.__name} | Account Number: {self.__account_number} | Total Amount: {self.__amo} | Password: {self.__pas}"
        
    
    def set_pass(self):
        if input("Enter Old Password: ") == self.__pas:
            pas = input("Enter New Password: ")
            self.__pas = pas
            print("Password Changed Successfull...")

    def get_pass(self):
        return self.__pas
    
    def set_depositeAmount(self):
        if input("Enter Password: ") == self.__pas:
            amo  = int(input("Enter the Deposite Amount: "))
            self.__amo += amo 
            print("Amount Deposited Successfull...")
        else:
            print("Wrong Password..")
            
    def get_amount(self):
        if input("Enter Password: ") == self.__pas:
            return self.__amo
        else:
            print("Wrong Password..")

u1 = Bank("Namrata Shinde",1005,"nam",0)

while(True):
    print(f"Account Details : 0 | Balance Check: 1 | Deposite Money: 2 | Password Change: 3 | Exit: 4")
    option = int(input(">>"))
    if option==0:
        print(u1.__str__())
    elif option == 1:
        print(f"Balance: {u1.get_amount()}")
    elif option ==2:
        u1.set_depositeAmount()
    elif option == 3:
        u1.set_pass()
    elif option == 4:
        break

class User:
    def __init__(self,un,ps):
        self.__username = un
        self.__password = ps
    def set_passwords(self,pas):
            if len(pas) >=8 and (i.isdigit() for i in pas):
                print("password is Correct...")
            else:
                print("Wroong")
u1 = User("Sai","yyy")   
u1.set_passwords("saieeeeee")
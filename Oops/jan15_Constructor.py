class student:
    def __init__(self,nm,r,c,s):
        print(f"Address of self is {id(self)}")
        self.name = nm
        self.roll_no = r
        self.city = c
        self.subject = s
s1 = student("Ram",1,"Pune","Python")
print(f"Address of s1 is {id(s1)}")
s2 = student("Sham",2,"Solapur","Java")
print(f"Address of s2 is {id(s2)}")

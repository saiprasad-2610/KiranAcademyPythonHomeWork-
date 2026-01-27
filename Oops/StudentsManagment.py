
class Student:
    def __init__(self,n,r):
        self.name = n
        self.roll = r
        self.marks = {}
    def addMarks(self,i):
        for j in range(i):
            subject = input("Enter the Subject: ")
            mark = int(input("Enter the Marks: "))
            self.marks[subject] = mark
        print("Marks added Successfully..")
    def displayMarks(self):
        print(self.marks)
    def studentDetails(self):
        print(f"Student Name: {self.name}\nStudent RollNo.: {self.roll}\nStudent Marks: {self.marks}  ")
    def calculatePercentage(self):
        print(f"Total Percentage is {(sum(self.marks.values()) /(len(self.marks)*100))* 100}")
    
s1 = Student("sai",10) 
print("....Welcome to Student Management.....")
print("Student Details: 0 | Add Marks: 1 | Display Marks: 2 | Percentage: 3 | Exit: 4 ")
while(True):
    i = int(input(">>"))
    if i==0:
        s1.studentDetails()
    elif i==1:
        s1.addMarks(int(input("Enter Number of Subjects: ")))
    elif i==2:
        s1.displayMarks()
    elif i==3:
        s1.calculatePercentage()
    elif i ==4:
        print("Thank You....")
        break

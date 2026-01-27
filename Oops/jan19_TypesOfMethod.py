# class student:
#     x=10
#     def __init__(self,r,n,m):
#         self.roll_no = r
#         self.name = n
#         self.marks = m
#     def getRoll(self):
#         return self.roll_no
#     def getName(self):
#         return self.name
#     def getMarks(self):
#         return self.marks
# s1 = student(1,"sai",85)
# print(f"Roll no is {s1.getMarks()}")
# print(f"Name is {s1.getName()}")
# print(f"Marks are {s1.getMarks()}")


class Player:
    def __init__(self,jn,n,r,w,t):
        self.jersey_no = jn
        self.name = n
        self.runs = r
        self.wickets = w
        self.team = t
# get data >>
    def getJerseyNo(self):
        return self.jersey_no
    def getPlayerName(self):
        return self.name
    def getRuns(self):
        return self.runs
    def getWickets(self):
        return self.wickets
    def getTeam(self):
        return self.team
    
    # Updates data >>
    def updateJerseyNo(self,new_jn):
        self.jersey_no = new_jn
    def updatePlayerName(self,new_n):
        self.name = new_n
    def updateRuns(self,new_r):
        self.runs = new_r
    def updateWickets(self,new_w):
        self.wickets = new_w
    def updateTeam(self,new_t):
        self.team = new_t    

p1 = Player(7,"M.S Dhoni,",17266,829,"CSK")
print(f"Name of Player: {p1.name} and total runs are {p1.runs} ")
p1.updateRuns(18000)
p1.updateWickets()
print(f"Name of Player: {p1.name} and total updated runs are {p1.runs} ")
